def calculate_rotation_command(bbox, screen_width, screen_height):
    bbox_center_x = (bbox[0] + bbox[2]) / 2
    bbox_center_y = (bbox[1] + bbox[3]) / 2
    
    screen_center_x = screen_width / 2
    screen_center_y = screen_height / 2
    
    distance_x = bbox_center_x - screen_center_x
    distance_y = bbox_center_y - screen_center_y
    print(distance_x)
    print(distance_y)
    
    rotation_commands = ""
    if distance_x > 0:
        rotation_commands += f"Rotate camera right by {distance_x} degrees.\n"
    elif distance_x < 0:
        rotation_commands += f"Rotate camera left by {-distance_x} degrees.\n"
    
    if distance_y > 0:
        rotation_commands += f"Rotate camera up by {distance_y} degrees.\n"
    elif distance_y < 0:
        rotation_commands += f"Rotate camera down by {-distance_y} degrees.\n"
    
    return rotation_commands

