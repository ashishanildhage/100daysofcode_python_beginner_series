# #Hurdles 3 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def rotate():
#     turn_left()
#     turn_left()
#     turn_left()

# def cycle():
#     turn_left()
#     move()
#     rotate()
#     move()
#     rotate()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         cycle()
    
# # #Maze
# def rotate():
#     turn_left()
#     turn_left() 
#     turn_left()
    
# while not at_goal():
#     if front_is_clear() and not right_is_clear():
#         move()
#     if wall_on_right() and front_is_clear():
#         move()            
#     elif wall_on_right() and wall_in_front():
#         turn_left()
#     elif at_goal():
#         break
#     elif (right_is_clear() or wall_in_front()):
#         rotate()
#         move()
#     else:
#             move()
           