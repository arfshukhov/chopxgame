screen take_gasmask_screen:
    imagebutton:
        idle "staff_design/take_mask_button.png"
        hover "staff_design/take_mask_button_hover.png"
        xsize 600
        ysize 130
        xalign 0.1
        yalign 0.5
        action partial(Inventory.take_item, GasMask), Hide("take_gasmask_screen"), partial(GasMask.make_taken), partial(Inventory.sub_slots), Jump("take_gasmask_result")
    imagebutton:
        idle "staff_design/pass_button.png"
        hover "staff_design/pass_button_hover.png"
        xsize 600
        ysize 130
        xalign 0.8
        yalign 0.5
        action Hide("take_gasmask_screen"), Jump("take_gasmask_result")


screen take_knife_screen:
    imagebutton:
        idle "staff_design/take_knife_button.png"
        hover "staff_design/take_knife_button_hover.png"
        xalign 0.1
        yalign 0.5
        action partial(Inventory.take_item, Knife), Hide("take_knife_screen"), partial(Knife.make_taken), partial(Inventory.sub_slots), Jump("take_knife_result")
    imagebutton:
        idle "staff_design/pass_button.png"
        hover "staff_design/pass_button_hover.png"
        xalign 0.8
        yalign 0.5
        action Hide("take_knife_screen"), Jump("take_knife_result")


screen take_medkit_screen:
    imagebutton:
        idle "staff_design/take_medkit_button.png"
        hover "staff_design/take_medkit_button_hover.png"
        xalign 0.1
        yalign 0.5
        action partial(Inventory.take_item, MedKit), Hide("take_medkit_screen"), partial(MedKit.make_taken), partial(Inventory.sub_slots), Jump("take_medkit_result")
    imagebutton:
        idle "staff_design/pass_button.png"
        hover "staff_design/pass_button_hover.png"
        xalign 0.8
        yalign 0.5
        action Hide("take_medkit_screen"), Jump("take_medkit_result")


screen take_flashlight_screen:
    imagebutton:
        idle "staff_design/take_flashlight_button.png"
        hover "staff_design/take_flashlight_button_hover.png"
        xalign 0.1
        yalign 0.5
        action partial(Inventory.take_item, Flashlight), Hide("take_flashlight_screen"), partial(Flashlight.make_taken), partial(Inventory.sub_slots), Jump("take_flashlight_result")
    imagebutton:
        idle "staff_design/pass_button.png"
        hover "staff_design/pass_button_hover.png"
        xalign 0.8
        yalign 0.5
        action Hide("take_flashlight_screen"), Jump("take_flashlight_result")


screen take_signal_pistol_screen:
    imagebutton:
        idle "staff_design/take_signal_pistol_button.png"
        hover "staff_design/take_signal_pistol_button_hover.png"
        xalign 0.1
        yalign 0.5
        action partial(Inventory.take_item, SignalPistol), Hide("take_signal_pistol_screen"), partial(SignalPistol.make_taken), partial(Inventory.sub_slots), Jump("take_signal_pistol_result")
    imagebutton:
        idle "staff_design/pass_button.png"
        hover "staff_design/pass_button_hover.png"
        xalign 0.8
        yalign 0.5
        action Hide("take_signal_pistol_screen"), Jump("take_signal_pistol_result")


screen inventory_screen:
    vbox:
        align (0.9, 0.2)
        text repr(inventory.inventory_set[0])
        
        