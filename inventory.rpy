init python:
    from functools import partial

    class InventoryItem:
        name: str
        taken: bool

        @classmethod
        def get_name(cls):
            return cls.name    

        @classmethod
        def make_taken(cls):
            cls.taken = True


    class GasMask(InventoryItem):
        name = "gas_mask"
        taken = False
    
    class Knife(InventoryItem):
        name = "knife"
        taken = False


    class MedKit(InventoryItem):
        name = "med_kit"
        taken = False


    class  Flashlight(InventoryItem):
        name = "flashlight"
        taken = False
    

    class SignalPistol(InventoryItem):
        name = "signal_pistol"
        taken = False
        

    class Inventory:
        inventory_set = set()
        empty_inventory_slots = 4
        def __init__(self):
            pass
        
        @classmethod
        def take_item(cls, item: InventoryItem):
            cls.inventory_set.add(item)
        
        @classmethod
        def sub_slots(cls):
            cls.empty_inventory_slots -= 1