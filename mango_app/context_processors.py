"""
Context processors for the Mango Surveillance application.

This module contains context processors that add additional context
to all template renderings across the application.
"""

def active_menu(request):
    """
    Add active menu information to templates.
    
    This context processor determines which section is active based on the
    current URL path and returns the section name.
    
    Args:
        request: The HTTP request object
        
    Returns:
        dict: A dictionary containing the active section name
    """
    path = request.path
    
    # Determine which section is active based on the path
    active_section = ''
    if path == '/':
        active_section = 'home'
    elif '/mango-items/' in path:
        active_section = 'mango_items'
    elif '/surveillance/' in path:
        active_section = 'surveillance'
    elif '/about/' in path:
        active_section = 'about'
    
    return {
        'active_section': active_section
    }