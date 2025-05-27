"""
Data repository for the Mango Surveillance application.

This module contains the data objects and helper functions for accessing
pest and disease information in the application. In a real-world application,
this data would likely come from a database.
"""
from .data_models import (MangoItem, TeamMember, EnvironmentalFactor, MangoFact, SurveillancePeriod,
                          SurveillanceMethod, RecordSheetField, SurveillanceRecommendation,
                          ExternalResource, ContactInformation)

# ======================================================================
# DATA: Mango Pests and Diseases
# ======================================================================

# Collection of all mango pests and diseases
mango_items = [
    # === PESTS ===
    MangoItem(
        id=1,
        name="Mango Seed Weevil", 
        scientific_name="Sternochetus mangiferae", 
        description="The adult weevil is 7-9 mm long, brown-black in color. It damages the mango seed, impacting fruit quality and export potential.",
        image_path="mango_app/images/mango_seed_weevil.jpg",
        item_type="pest",
        detailed_info="The mango seed weevil is a major quarantine pest of mangoes. The adult is 7-9 mm long, brown-black in color with light patterns on its back. The female lays eggs on developing fruit, and larvae tunnel into the seed where they develop. Affected fruit show no external symptoms, making detection difficult. The pest reduces seed viability and can cause premature fruit drop. Most damage is to the seed rather than the flesh, but infestation prevents export to many countries with quarantine restrictions."
    ),
    MangoItem(
        id=2,
        name="Mango Fruit Fly", 
        scientific_name="Bactrocera dorsalis", 
        description="A serious pest that lays eggs in ripening fruit. The larvae feed on the fruit pulp, causing decay and fruit drop.",
        image_path="mango_app/images/mango_fruit_fly.jpg",
        item_type="pest",
        detailed_info="The mango fruit fly is a significant pest that affects ripening mangoes. Adult flies are about 8mm long with clear wings marked with a dark stripe along the front margin. Females lay eggs under the skin of ripening fruit. The hatched larvae (maggots) feed on the fruit pulp, causing decay and creating an entry point for secondary infections. Infested fruit often shows small puncture marks, softening, and premature dropping. The fruit fly is highly mobile and can spread rapidly. It's a major quarantine concern, restricting export opportunities for affected regions."
    ),
    MangoItem(
        id=3,
        name="Mango Leaf Hopper", 
        scientific_name="Idioscopus spp.", 
        description="Small insects that feed on plant sap from young shoots, leaves, and inflorescences.",
        image_path="mango_app/images/mango_leaf_hopper.jpg",
        item_type="pest",
        detailed_info="Mango leafhoppers are small wedge-shaped insects about 3-5mm long that feed on plant sap from young shoots, leaves, and inflorescences. They're often light green to brownish in color and can jump or fly short distances when disturbed. These pests use piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf curl, and reduced vigor. Their feeding on flower panicles can result in flower drop and reduced fruit set. Additionally, they excrete honeydew which promotes the growth of sooty mold. Heavy infestations during flowering can significantly reduce yield. These pests thrive in warm, humid conditions typical of mango growing regions."
    ),
    MangoItem(
        id=4,
        name="Mango Scale Insect", 
        scientific_name="Aulacaspis tubercularis", 
        description="Small, immobile insects that attach to plant parts and feed on sap.",
        image_path="mango_app/images/mango_scale_insect.jpg",
        item_type="pest",
        detailed_info="Mango scale insects are small, immobile pests that attach themselves to leaves, branches, and sometimes fruit of mango trees. The white mango scale (Aulacaspis tubercularis) is a common species affecting mangoes. Adult females are covered with a circular or oyster-shaped waxy shield about 2-3mm in diameter, typically white or light gray. Males are smaller with an elongated covering. These insects use their piercing-sucking mouthparts to extract plant sap, causing yellowing, leaf drop, and dieback of branches in severe infestations. They can also affect fruit appearance, reducing marketability. Scale insects excrete honeydew, leading to sooty mold growth. Heavy infestations weaken trees and can reduce yields. They're difficult to control due to their protective waxy covering."
    ),
    
    # === DISEASES ===
    MangoItem(
        id=5,
        name="Anthracnose", 
        scientific_name="Colletotrichum gloeosporioides", 
        description="A fungal disease affecting mangoes in all growth stages, particularly in humid conditions.",
        image_path="mango_app/images/anthracnose.jpg",
        item_type="disease",
        detailed_info="Anthracnose is a major fungal disease of mangoes caused by Colletotrichum gloeosporioides. It affects leaves, flowers, and fruits at all stages of development. On leaves, it appears as irregular dark spots that may coalesce and cause defoliation. On flowers, it causes blackening and blossom blight, reducing fruit set. On developing fruit, it creates small, dark, sunken spots that remain dormant until ripening, when they enlarge and cause fruit rot. Mature fruit can develop large, sunken, dark lesions with pinkish-orange spore masses in humid conditions. The disease is favored by warm, wet weather and can cause significant losses in both yield and quality. It's particularly problematic in humid tropical and subtropical regions."
    ),
    MangoItem(
        id=6,
        name="Powdery Mildew", 
        scientific_name="Oidium mangiferae", 
        description="A fungal disease that affects flowers and young fruits, causing significant yield loss.",
        image_path="mango_app/images/powdery_mildew.jpg",
        item_type="disease",
        detailed_info="Powdery mildew in mangoes is caused by the fungus Oidium mangiferae. It primarily affects inflorescences (flower panicles), young fruits, and new leaves. The disease appears as a white, powdery coating on affected plant parts. Infected flowers may dry up and fall off, significantly reducing fruit set. Young fruits may be distorted, stunted, or drop prematurely if infected. The disease can cause up to 80% yield loss in severe cases. Unlike many fungal diseases, powdery mildew can develop in relatively dry conditions with high humidity, though free water inhibits spore germination. It's particularly severe during flowering and fruit set periods when temperatures are moderate (20-25°C). The disease spreads rapidly via airborne spores."
    ),
    MangoItem(
        id=7,
        name="Bacterial Black Spot", 
        scientific_name="Xanthomonas campestris pv. mangiferaeindicae", 
        description="A bacterial disease that causes black lesions on leaves, stems, and fruits.",
        image_path="mango_app/images/bacterial_black_spot.jpg",
        item_type="disease",
        detailed_info="Bacterial black spot, caused by Xanthomonas campestris pv. mangiferaeindicae, is a serious disease affecting mangoes in many growing regions. On leaves, it appears as small, angular, water-soaked lesions that become black, necrotic spots with yellow halos. These can coalesce during severe infections, causing leaf blight. On stems and branches, it causes raised black lesions that may crack and exude gum. Fruit symptoms include small, black, raised spots that may develop into corky, star-shaped cracks with bacterial ooze. The disease reduces tree vigor, fruit quality, and marketability. It spreads through rain splash, wind-driven rain, and contaminated plant material. Warm temperatures (25-30°C) and high humidity favor disease development. It's particularly severe in wet tropical and subtropical regions."
    )
]


# Team members data
team_members = [
    TeamMember('Arpan Nepal', '371945'),
    TeamMember('Samir Bajgain', '369784'),
    TeamMember('Abdullah AL mahmud Didar', '386212'),
    TeamMember('Abishek Kandel', '387576'),
]

# Environmental factors data
environmental_factors = [
    EnvironmentalFactor('Anthracnose', '25-28°C', 'High (>80%)', 'High', 'Wet season'),
    EnvironmentalFactor('Powdery Mildew', '20-25°C', 'Low to moderate', 'Low', 'Dry season'),
    EnvironmentalFactor('Bacterial Black Spot', '25-30°C', 'High', 'High', 'Wet season'),
]

# Interesting facts about mangoes
mango_facts = [
    MangoFact("Australia's mango industry produces over 70,000 tonnes of mangoes annually, with a farm gate value exceeding $200 million."),
    MangoFact("Early detection of pests and diseases can save growers thousands of dollars in lost production."),
    MangoFact("Regular monitoring during critical periods like flowering and fruiting is essential for effective pest and disease management."),
]

# Surveillance calendar periods
surveillance_periods = [
    SurveillancePeriod('Pre-flowering', 'June-July', 'medium'),
    SurveillancePeriod('Flowering', 'August-September', 'high'),
    SurveillancePeriod('Fruit Development', 'October-November', 'high'),
    SurveillancePeriod('Harvest', 'December-February', 'medium'),
    SurveillancePeriod('Post-harvest', 'March-May', 'low'),
]

# Surveillance methods
surveillance_methods = [
    SurveillanceMethod(
        name="Visual Inspection",
        description="Regular visual examination of trees for signs of pests and diseases.",
        best_for=["General monitoring", "Early detection"],
        frequency="Weekly during critical growth stages, monthly otherwise.",
        procedure="Systematically check leaves, branches, flowers, and fruits for abnormalities."
    ),
    SurveillanceMethod(
        name="Trapping",
        description="Using various traps to monitor and detect pest presence.",
        best_for=["Flying insects", "Population monitoring"],
        frequency="Check traps weekly, replace as needed.",
        procedure="Place pheromone traps, sticky traps, or light traps at strategic locations in the orchard."
    ),
    SurveillanceMethod(
        name="Sampling",
        description="Collection of plant material for closer examination or laboratory testing.",
        best_for=["Disease confirmation", "Detailed analysis"],
        frequency="As needed, especially when symptoms are observed.",
        procedure="Collect affected plant parts in sealed bags and send to a diagnostic laboratory."
    ),
    SurveillanceMethod(
        name="Systematic Monitoring",
        description="Following a structured schedule and methodology for surveillance.",
        best_for=["Comprehensive coverage", "Regulatory compliance"],
        frequency="According to established protocols, typically monthly.",
        procedure="Divide orchard into monitoring zones, record observations using standardized forms."
    )
]

# Record sheet fields
record_sheet_fields = [
    RecordSheetField("Date", "Date of surveillance activity"),
    RecordSheetField("Block/Zone", "Specific area monitored"),
    RecordSheetField("Trees Inspected", "Number and identification of trees checked"),
    RecordSheetField("Plant Parts Checked", "Leaves, branches, flowers, fruits, trunk"),
    RecordSheetField("Observations", "Symptoms, pests seen, severity, distribution"),
    RecordSheetField("Weather", "Temperature, humidity, rainfall, wind"),
    RecordSheetField("Actions Taken", "Samples collected, treatments applied"),
    RecordSheetField("Inspector", "Name of person conducting surveillance"),
]

# Surveillance recommendations
surveillance_recommendations = [
    SurveillanceRecommendation(
        item_type="pest",
        recommendations=[
            "Conduct regular inspections at least once every two weeks during critical growth periods.",
            "Pay special attention to new growth, flowering parts, and developing fruit.",
            "Use a hand lens to inspect for small pests like scale insects and mites.",
            "Install and regularly check pest traps (sticky traps, pheromone traps).",
            "Keep records of all observations, including pest-free inspections."
        ]
    ),
    SurveillanceRecommendation(
        item_type="disease",
        recommendations=[
            "Monitor trees weekly during flowering and fruit development stages.",
            "Increase monitoring frequency during wet and humid conditions.",
            "Examine both upper and lower leaf surfaces for disease symptoms.",
            "Sample suspicious plant material for laboratory diagnosis when needed.",
            "Keep detailed records of all observations, including weather conditions."
        ]
    )
]

# External resources
external_resources = [
    ExternalResource(
        name="Australian Department of Agriculture, Fisheries and Forestry - Biosecurity",
        url="https://www.agriculture.gov.au/abares/products/insights/snapshot-of-australian-agriculture#agricultural-production-is-growing"
    ),
    ExternalResource(
        name="Australian Mango Industry Association",
        url="https://www.industry.mangoes.net.au/"
    ),
    ExternalResource(
        name="Plant Health Australia",
        url="https://www.planthealthaustralia.com.au/wp-content/uploads/2024/01/Mango-fruit-borer-FS.pdf"
    )
]

# Contact information
contact_info = ContactInformation(
    name="HIT237 Course Coordinator",
    organization="Charles Darwin University",
    address="Darwin, NT 0909",
    email="hit237@cdu.edu.au",
    phone="(08) 8946 XXXX"
)

# ======================================================================
# DATA ACCESS FUNCTIONS
# ======================================================================

def get_item_by_id(item_id):
    """
    Retrieve a mango item by its ID.
    
    Args:
        item_id (int): The ID of the item to retrieve
        
    Returns:
        MangoItem: The matching item or None if not found
    """
    for item in mango_items:
        if item.id == item_id:
            return item
    return None

def get_team_members():
    """
    Retrieve the list of team members.
    
    Returns:
        list: List of TeamMember objects
    """
    return team_members

def get_environmental_factors():
    """
    Retrieve the list of environmental factors affecting disease development.
    
    Returns:
        list: List of EnvironmentalFactor objects
    """
    return environmental_factors

def get_mango_facts():
    """
    Retrieve the list of interesting mango facts.
    
    Returns:
        list: List of MangoFact objects
    """
    return mango_facts

def get_surveillance_periods():
    """
    Retrieve the list of surveillance periods.
    
    Returns:
        list: List of SurveillancePeriod objects
    """
    return surveillance_periods

def get_surveillance_methods():
    """
    Retrieve the list of surveillance methods.
    
    Returns:
        list: List of SurveillanceMethod objects
    """
    return surveillance_methods

def get_record_sheet_fields():
    """
    Retrieve the list of record sheet fields.
    
    Returns:
        list: List of RecordSheetField objects
    """
    return record_sheet_fields

def get_surveillance_recommendations(item_type=None):
    """
    Retrieve surveillance recommendations, optionally filtered by item type.
    
    Args:
        item_type (str, optional): Filter by 'pest' or 'disease'. Defaults to None.
        
    Returns:
        list: List of SurveillanceRecommendation objects, filtered by item_type if provided
        
    Raises:
        ValueError: If item_type is not one of the valid types
    """
    valid_types = ('pest', 'disease')
    
    # If item_type is provided, validate it
    if item_type is not None and item_type not in valid_types:
        raise ValueError(f"item_type must be one of {valid_types}")
    
    # If no item_type provided, return all recommendations
    if item_type is None:
        return surveillance_recommendations
        
    # Filter recommendations by item_type
    filtered_recs = [rec for rec in surveillance_recommendations if rec.item_type == item_type]
    return filtered_recs

def get_external_resources():
    """
    Retrieve the list of external resources.
    
    Returns:
        list: List of ExternalResource objects
    """
    return external_resources

def get_contact_info():
    """
    Retrieve the contact information.
    
    Returns:
        ContactInformation: Contact information object
    """
    return contact_info


