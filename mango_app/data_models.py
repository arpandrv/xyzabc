"""
Data models for the Mango Surveillance application.

This module defines the model classes for representing pests, diseases,
and other entities in the application.
"""

class MangoItem:
    """
    Class representing a pest or disease affecting mangoes.
    
    This is a data model class that stores information about mango pests
    and diseases, including their names, descriptions, images, and detailed
    information for educational purposes.
    """
    
    # Valid item types
    ITEM_TYPES = ('pest', 'disease')
    
    def __init__(self, id, name, scientific_name, description, image_path, item_type, detailed_info):
        """
        Initialize a MangoItem object.
        
        Args:
            id (int): Unique identifier for the item
            name (str): Common name of the pest or disease
            scientific_name (str): Scientific name of the pest or disease
            description (str): Brief description for overview display
            image_path (str): Path to the image file
            item_type (str): Either 'pest' or 'disease'
            detailed_info (str): Detailed information about the pest or disease
        
        Raises:
            ValueError: If item_type is not 'pest' or 'disease'
        """
        # Validate item_type
        if item_type not in self.ITEM_TYPES:
            raise ValueError(f"item_type must be one of {self.ITEM_TYPES}")
            
        # Assign instance attributes
        self.id = id
        self.name = name
        self.scientific_name = scientific_name
        self.description = description
        self.image_path = image_path
        self.item_type = item_type
        self.detailed_info = detailed_info
    
    def get_item_type_display(self):
        """
        Return the display name for the item type.
        
        Returns:
            str: 'Pest' or 'Disease' based on the item_type property
        """
        return "Pest" if self.item_type == "pest" else "Disease"
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Item name and type in parentheses
        """
        return f"{self.name} ({self.get_item_type_display()})"


class TeamMember:
    """
    Class representing a team member who contributed to the project.
    """
    
    def __init__(self, name, student_id):
        """
        Initialize a TeamMember object.
        
        Args:
            name (str): Name of the team member
            student_id (str): Student ID of the team member
        """
        self.name = name
        self.student_id = student_id
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Team member name and student ID
        """
        return f"{self.name} (ID: {self.student_id})"


class EnvironmentalFactor:
    """
    Class representing environmental factors affecting disease development.
    """
    
    def __init__(self, disease, temperature, humidity, rainfall, season):
        """
        Initialize an EnvironmentalFactor object.
        
        Args:
            disease (str): Name of the disease
            temperature (str): Temperature range affecting the disease
            humidity (str): Humidity level affecting the disease
            rainfall (str): Rainfall level affecting the disease
            season (str): Season when the disease is most prevalent
        """
        self.disease = disease
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall
        self.season = season
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Disease name and environmental conditions
        """
        return f"{self.disease} ({self.temperature}, {self.humidity} humidity)"


class MangoFact:
    """
    Class representing an interesting fact about the mango industry.
    """
    
    def __init__(self, content):
        """
        Initialize a MangoFact object.
        
        Args:
            content (str): The fact content
        """
        self.content = content
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: The fact content
        """
        return self.content


class SurveillancePeriod:
    """
    Class representing a surveillance period with its risk level.
    """
    
    # Valid risk levels
    RISK_LEVELS = ('low', 'medium', 'high')
    
    def __init__(self, name, months, risk_level):
        """
        Initialize a SurveillancePeriod object.
        
        Args:
            name (str): Name of the period (e.g., 'Pre-flowering')
            months (str): Month range (e.g., 'June-July')
            risk_level (str): Risk level ('low', 'medium', 'high')
            
        Raises:
            ValueError: If risk_level is not valid
        """
        if risk_level not in self.RISK_LEVELS:
            raise ValueError(f"risk_level must be one of {self.RISK_LEVELS}")
            
        self.name = name
        self.months = months
        self.risk_level = risk_level
        
    def get_display_text(self):
        """
        Get the display text for this period.
        
        Returns:
            str: Period name with months
        """
        return f"{self.name} ({self.months})"
    
    def get_risk_tag_class(self):
        """
        Get the CSS class for this risk level.
        
        Returns:
            str: CSS class for styling
        """
        return f"{self.risk_level}-risk"
    
    def get_risk_display(self):
        """
        Get the display text for the risk level.
        
        Returns:
            str: Capitalized risk level
        """
        return f"{self.risk_level.capitalize()} Risk"
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Period name, months, and risk level
        """
        return f"{self.name} ({self.months}): {self.get_risk_display()}"


class SurveillanceMethod:
    """
    Class representing a surveillance method for mango pests and diseases.
    """
    
    def __init__(self, name, description, best_for, frequency, procedure):
        """
        Initialize a SurveillanceMethod object.
        
        Args:
            name (str): Name of the method
            description (str): Brief description of the method
            best_for (list): List of what the method is best for
            frequency (str): Recommended frequency
            procedure (str): Basic procedure description
        """
        self.name = name
        self.description = description
        self.best_for = best_for
        self.frequency = frequency
        self.procedure = procedure
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Method name
        """
        return self.name


class RecordSheetField:
    """
    Class representing a field in a surveillance record sheet.
    """
    
    def __init__(self, field_name, description):
        """
        Initialize a RecordSheetField object.
        
        Args:
            field_name (str): Name of the field
            description (str): Description of what to record
        """
        self.field_name = field_name
        self.description = description
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Field name
        """
        return self.field_name


class SurveillanceRecommendation:
    """
    Class representing a surveillance recommendation.
    """
    
    # Valid item types - same as MangoItem
    ITEM_TYPES = ('pest', 'disease')
    
    def __init__(self, item_type, recommendations):
        """
        Initialize a SurveillanceRecommendation object.
        
        Args:
            item_type (str): Type of item ('pest' or 'disease')
            recommendations (list): List of recommendation strings
            
        Raises:
            ValueError: If item_type is not 'pest' or 'disease'
        """
        # Validate item_type
        if item_type not in self.ITEM_TYPES:
            raise ValueError(f"item_type must be one of {self.ITEM_TYPES}")
            
        self.item_type = item_type
        self.recommendations = recommendations
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Item type and number of recommendations
        """
        return f"{self.item_type.capitalize()} recommendations ({len(self.recommendations)})"


class ExternalResource:
    """
    Class representing an external resource link.
    """
    
    def __init__(self, name, url):
        """
        Initialize an ExternalResource object.
        
        Args:
            name (str): Name of the resource
            url (str): URL of the resource
        """
        self.name = name
        self.url = url
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Resource name
        """
        return self.name


class ContactInformation:
    """
    Class representing contact information.
    """
    
    def __init__(self, name, organization, address, email, phone):
        """
        Initialize a ContactInformation object.
        
        Args:
            name (str): Contact name or title
            organization (str): Organization name
            address (str): Physical address
            email (str): Email address
            phone (str): Phone number
        """
        self.name = name
        self.organization = organization
        self.address = address
        self.email = email
        self.phone = phone
    
    def __str__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: Contact name and organization
        """
        return f"{self.name}, {self.organization}"