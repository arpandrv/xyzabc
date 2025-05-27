from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import SurveySession, SurveillanceCalculation
from core.season_utils import get_seasonal_stage_info
from core.calculations import calculate_surveillance_effort, DEFAULT_CONFIDENCE
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fix survey sessions that have missing or zero target_plants_surveyed'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be fixed without actually making changes'
        )
        parser.add_argument(
            '--status',
            type=str,
            default='in_progress',
            help='Status of sessions to fix (default: in_progress)'
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        status_filter = options['status']
        
        # Find sessions with missing targets
        sessions_to_fix = SurveySession.objects.filter(
            status=status_filter,
            target_plants_surveyed__isnull=True
        ).select_related('farm')
        
        # Also find sessions with zero targets
        zero_target_sessions = SurveySession.objects.filter(
            status=status_filter,
            target_plants_surveyed=0
        ).select_related('farm')
        
        all_sessions = list(sessions_to_fix) + list(zero_target_sessions)
        
        if not all_sessions:
            self.stdout.write(
                self.style.SUCCESS(f'No {status_filter} sessions found with missing or zero targets.')
            )
            return
        
        self.stdout.write(f'Found {len(all_sessions)} sessions that need target fixes:')
        
        fixed_count = 0
        error_count = 0
        
        for session in all_sessions:
            farm = session.farm
            original_target = session.target_plants_surveyed
            
            try:
                # Try to get target from current calculation
                target_plants = None
                try:
                    latest_calc = SurveillanceCalculation.objects.filter(
                        farm=farm, 
                        is_current=True
                    ).latest('date_created')
                    target_plants = latest_calc.required_plants
                    source = f"saved calculation (ID: {latest_calc.id})"
                except SurveillanceCalculation.DoesNotExist:
                    # Calculate a default target
                    if farm.total_plants():
                        seasonal_info = get_seasonal_stage_info()
                        prevalence_p = seasonal_info.get('prevalence_p')
                        if prevalence_p is not None:
                            calculation_results = calculate_surveillance_effort(
                                farm=farm,
                                confidence_level_percent=DEFAULT_CONFIDENCE,
                                prevalence_p=prevalence_p
                            )
                            if not calculation_results.get('error'):
                                target_plants = calculation_results['required_plants_to_survey']
                                source = "calculated default"
                            else:
                                source = f"calculation error: {calculation_results.get('error')}"
                        else:
                            source = "no seasonal prevalence data"
                    else:
                        source = "no farm plant count"
                
                # Fallback target
                if target_plants is None and farm.total_plants() and farm.total_plants() > 0:
                    target_plants = max(1, min(5, farm.total_plants() // 10))
                    source = "fallback (10% of plants, min 1, max 5)"
                
                if target_plants is not None:
                    if dry_run:
                        self.stdout.write(f'  Would fix session {session.session_id} on {farm.name}:')
                        self.stdout.write(f'    Original target: {original_target} → New target: {target_plants}')
                        self.stdout.write(f'    Source: {source}')
                    else:
                        session.target_plants_surveyed = target_plants
                        session.save(update_fields=['target_plants_surveyed'])
                        self.stdout.write(f'  Fixed session {session.session_id} on {farm.name}:')
                        self.stdout.write(f'    Target: {original_target} → {target_plants} (from {source})')
                    fixed_count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(f'  Cannot fix session {session.session_id} on {farm.name}: {source}')
                    )
                    error_count += 1
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'  Error fixing session {session.session_id}: {e}')
                )
                error_count += 1
        
        if dry_run:
            self.stdout.write(f'\nDRY RUN: Would fix {fixed_count} sessions, {error_count} could not be fixed')
            self.stdout.write('Run without --dry-run to apply changes')
        else:
            self.stdout.write(f'\nFixed {fixed_count} sessions successfully')
            if error_count > 0:
                self.stdout.write(f'{error_count} sessions could not be fixed')
        
        # Additional info about how to use the command
        self.stdout.write('\nTip: You can also fix completed sessions with --status=completed')