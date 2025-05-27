from django.contrib import admin
from .models import (
    Grower, Farm, Region, PlantType, PlantPart, Pest, Disease, 
    SeasonalStage, SurveySession, Observation, SurveillanceCalculation
)

@admin.register(Grower)
class GrowerAdmin(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'contact_number']  # Changed from 'farm_name' to 'business_name'
    search_fields = ['user__username', 'user__email', 'business_name']
    list_filter = ['user__date_joined']
    readonly_fields = ['user']

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'region', 'size_hectares', 'stocking_rate', 'total_plants']
    search_fields = ['name', 'owner__user__username', 'formatted_address']
    list_filter = ['region', 'plant_type']
    readonly_fields = ['total_plants']
    
    def total_plants(self, obj):
        return obj.total_plants()
    total_plants.short_description = 'Total Plants'

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'climate_zone', 'state_abbreviation']
    search_fields = ['name', 'climate_zone']

@admin.register(PlantType)
class PlantTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(PlantPart)
class PlantPartAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    filter_horizontal = ['affects_plant_types', 'affects_plant_parts']

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    filter_horizontal = ['affects_plant_types', 'affects_plant_parts']

@admin.register(SeasonalStage)
class SeasonalStageAdmin(admin.ModelAdmin):
    list_display = ['name', 'months', 'prevalence_p']
    search_fields = ['name']
    filter_horizontal = ['active_pests', 'active_diseases']

@admin.register(SurveySession)
class SurveySessionAdmin(admin.ModelAdmin):
    list_display = ['farm', 'surveyor', 'start_time', 'end_time', 'status', 'observation_count']
    search_fields = ['farm__name', 'surveyor__username']
    list_filter = ['status', 'start_time']
    readonly_fields = ['session_id', 'observation_count']
    
    def observation_count(self, obj):
        return obj.observation_count()
    observation_count.short_description = 'Observations'

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['session', 'plant_sequence_number', 'observation_time', 'status', 'has_pests', 'has_diseases']
    search_fields = ['session__farm__name', 'notes']
    list_filter = ['status', 'observation_time']
    filter_horizontal = ['pests_observed', 'diseases_observed']
    
    def has_pests(self, obj):
        return obj.has_pests()
    has_pests.boolean = True
    has_pests.short_description = 'Pests Found'
    
    def has_diseases(self, obj):
        return obj.has_diseases()
    has_diseases.boolean = True
    has_diseases.short_description = 'Diseases Found'

@admin.register(SurveillanceCalculation)
class SurveillanceCalculationAdmin(admin.ModelAdmin):
    list_display = ['farm', 'created_by', 'date_created', 'season', 'confidence_level', 'required_plants', 'is_current']
    search_fields = ['farm__name', 'created_by__username']
    list_filter = ['season', 'confidence_level', 'is_current', 'date_created']
    readonly_fields = ['date_created']