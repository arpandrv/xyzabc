"""
Views for the Mango Surveillance application.

This module contains the view classes for displaying pages and handling
user requests for the Mango Pest and Disease Surveillance web application.
"""
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import Http404

from .data import (mango_items, get_item_by_id, get_team_members, get_environmental_factors,
                 get_mango_facts, get_surveillance_periods, get_surveillance_methods,
                 get_record_sheet_fields, get_surveillance_recommendations,
                 get_external_resources, get_contact_info)

# Home Page View
class HomeView(TemplateView):
    """Display the home page with featured content."""
    template_name = 'mango_app/home.html'
    
    def get_context_data(self, **kwargs):
        """
        Add mango facts and surveillance periods to the template context.
        
        Returns:
            dict: Template context with mango facts and surveillance periods
        
        Raises:
            Http404: If required data is not available
        """
        context = super().get_context_data(**kwargs)
        
        # Get mango facts
        facts = get_mango_facts()
        if not facts:
            raise Http404("Mango facts data is unavailable")
            
        # Get surveillance periods
        periods = get_surveillance_periods()
        if not periods:
            raise Http404("Surveillance periods data is unavailable")
            
        context['mango_facts'] = facts
        context['surveillance_periods'] = periods
        return context


# Pest and Disease List View
class MangoItemListView(TemplateView):
    """Display all pests and diseases in a grid layout."""
    template_name = 'mango_app/mango_items.html'
    
    def get_context_data(self, **kwargs):
        """
        Add mango items to the template context.
        
        Returns:
            dict: Template context with mango items and environmental factors
        
        Raises:
            Http404: If no mango items are available
        """
        context = super().get_context_data(**kwargs)
        
        # Check if mango items exist
        if not mango_items:
            raise Http404("No mango pests or diseases available")
        
        # Add environmental factors
        env_factors = get_environmental_factors()
        if not env_factors:
            raise Http404("Environmental factors data is unavailable")
            
        context['mango_items'] = mango_items
        context['environmental_factors'] = env_factors
        return context


# Individual Pest or Disease Detail View
class MangoItemDetailView(View):
    """Display detailed information about a specific pest or disease."""
    template_name = 'mango_app/detail.html'
    
    def get(self, request, item_id):
        """
        Handle GET requests for a specific mango item detail page.
        
        Args:
            request: The HTTP request
            item_id: The ID of the mango item to display
            
        Returns:
            Rendered detail template with the item context
            
        Raises:
            Http404: If item ID is invalid or item not found
        """
        # Convert ID to integer
        try:
            item_id = int(item_id)
        except ValueError:
            raise Http404("Invalid item ID")
        
        # Get the item
        item = get_item_by_id(item_id)
        if not item:
            raise Http404("Item not found")
        
        # Get recommendations for this item type
        try:
            recommendations = get_surveillance_recommendations(item.item_type)
            if not recommendations:
                raise Http404(f"Recommendations for {item.item_type} not found")
                
            # Since we want a single recommendation object to access its properties
            # but the function now always returns a list, get the first match
            recommendation = recommendations[0] if recommendations else None
            
            if not recommendation:
                raise Http404(f"Recommendations for {item.item_type} not found")
            
            # Create context with item and recommendation
            context = {
                'item': item,
                'recommendation': recommendation
            }
        except ValueError as e:
            # Handle invalid item_type
            raise Http404(f"Invalid item type: {str(e)}")
        
        # Return the rendered template with context
        return render(request, self.template_name, context)


# Surveillance Methods View
class SurveillanceView(TemplateView):
    """Display information about surveillance methods for mango pests and diseases."""
    template_name = 'mango_app/surveillance.html'
    
    def get_context_data(self, **kwargs):
        """
        Add surveillance methods and record sheet fields to the template context.
        
        Returns:
            dict: Template context with surveillance data
            
        Raises:
            Http404: If required data is not available
        """
        context = super().get_context_data(**kwargs)
        
        # Get surveillance methods
        methods = get_surveillance_methods()
        if not methods:
            raise Http404("Surveillance methods data is unavailable")
            
        # Get record sheet fields
        fields = get_record_sheet_fields()
        if not fields:
            raise Http404("Record sheet fields data is unavailable")
            
        context['surveillance_methods'] = methods
        context['record_sheet_fields'] = fields
        return context


# About Project View
class AboutView(TemplateView):
    """Display information about the project and team members."""
    template_name = 'mango_app/about.html'
    
    def get_context_data(self, **kwargs):
        """
        Add team member information, external resources, and contact info to the template context.
        
        Returns:
            dict: Template context with team members and resources
            
        Raises:
            Http404: If required data is missing or corrupted
        """
        context = super().get_context_data(**kwargs)
        
        # Get team members from data module
        team_members = get_team_members()
        if not team_members:
            raise Http404("Team member information is unavailable")
            
        # Get external resources
        resources = get_external_resources()
        if not resources:
            raise Http404("External resources information is unavailable")
            
        # Get contact information
        contact = get_contact_info()
        if not contact:
            raise Http404("Contact information is unavailable")
            
        context['team_members'] = team_members
        context['external_resources'] = resources
        context['contact'] = contact
        return context