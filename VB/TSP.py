#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:25:46 2022

@author: Juan
"""
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from random import randint

# def RandPoints(intensidade):
#     Pontos = []
    
#     for _ in range(intensidade*2):
#         Pontos.append([randint(500,2000),randint(500,2000)])
#     return(Pontos)

# pontos = RandPoints(10)
# print(pontos)

starting=0 #Ponto inicial



def create_data_model(points,starting):
    """Stores the data for the problem."""
    data = {}
    # Locations in block units
    data['locations'] = points  
    data['num_vehicles'] = 1
    data['depot'] = starting
    return data


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    index = routing.Start(0)
    plan_output = []
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
   
    return plan_output
    


def main(points,starting=0):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(points,starting)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(data['locations'])

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        return print_solution(manager, routing, solution)

def TSP(points):
    permutation = main(points,starting=starting)
    points2=[]
    for i in permutation:
        points2.append(points[i])
    x, y = map(list,zip(*points2))

    return x, y

# PONTOS = [[0.6458052699575985, -0.8575687286066063], [1.1050588645416295, -0.8461994423240035], [2.2044238047231275, -0.9151589235042453], [3.1173462590160685, -0.5070728134017217], [4.824670014621365, -0.407979601616131], [5.2394395845561395, -0.8294825794581523], [6.2548846163238565, -0.4013474210633219], [7.857960368036603, -0.2391803031586105], [8.546642899443224, -0.7623633040033287], [9.74779670258294, -0.8770359602245229], [9.4185708838581, -1.91894456003482], [8.749145266327607, -1.202956093290557], [7.040955277263035, -1.5629804305922186], [7.1912524394036055, -1.3309873648717923], [6.366156050879508, -1.2333482233947899], [5.522826396519703, -1.3243660522015444], [4.269023568606225, -1.3612589897062835], [3.749105006400026, -1.8502105846017993], [2.257457094366228, -1.5030948359088536], [1.6751150182082704, -1.6824272783127332], [0.7810794671096476, -1.9747194403519859], [0.5232604404920386, -2.0471063078638654], [1.5677289712493185, -2.7869550250700845], [2.5244883916139873, 
# -2.6161071695850784], [3.3615170542623765, -2.0423689646797754], [4.53109308700782, -2.3090157945368714], [4.030407869198252, -2.710093989883561], [5.170297399762242, -2.5129730707913795], [6.153301832853383, -2.70998558233907], [7.254667228581165, -2.093961323795978], [8.895094377521431, -2.7463308323307682], [9.048075406301189, -2.3094841107995334], [9.35150694801291, -3.9456326025699227], [8.042877879771602, -3.61896121208659], [7.268447141968242, -3.7496070456927884], [7.238386956875814, -3.865863709099599], [6.703882711604169, -3.3328045510842905], [6.417765913933223, -3.747581362525524], [5.088020785322414, -3.442437501197049], [5.55238174690957, -3.5057225879973406], [4.192994252303637, -3.8455274351789646], [3.1149358926616553, -3.716751768328095], [2.649298706670923, -3.7712730193323476], [1.3635534279247428, -3.1697658362385672], [0.6117859270491842, -3.5555186276347204], [0.0586619177302129, -4.507157257307382], [1.6994165231885905, -4.746543416904068], [2.1917525311320087, -4.747339737430741], [3.7041458513675307, -4.030284595128427], [4.439869088055747, -4.035985717887077], [4.527359407000889, -4.163508330979842], [5.283939330455411, -4.599479914119134], [5.880778542144679, -4.938861218631977], [6.906540950577607, -4.181556271074045], [6.244596222615738, -4.228163246909773], [7.781524861058008, -4.229155013670359], [7.06175286399859, -4.71715307778263], [8.219850378016314, -4.909351265107276], [9.309762948006172, -4.450790664914557], [9.7533143976683, -5.957345745996542], [8.945076582545083, -5.279966694969733], [7.2418320698183285, -5.565913393980924], [7.158457671207422, -5.1638789499094555], [6.51349475978026, -5.3714858953605304], [6.412307991532639, -5.352929898654791], [5.3487495665743126, -5.1104981034548915], [5.047877257595896, -5.240299192251878], [4.7705806693332, -5.789236309105429], [4.751825469535004, 
# -5.707813168807493], [3.235655173709615, -5.857753727707037], [3.392576126332414, -5.323010747450397], [2.514724521966288, -5.238724751081198], [2.778971129987296, -5.303096831727636], [1.694758249627159, -5.113539606913654], [0.3400971388036945, -5.016545069197647], [0.9903456959118311, -6.1353561908015415], [1.6849401821913617, -6.149940873294427], [2.497091197080497, -6.459500901361798], [2.209088468654392, -6.5793859398212], [3.809601989291422, -6.688034545694499], [3.4017969790548683, -6.0884731815515085], [4.6624028737687135, -6.478188477480843], [4.266243931474165, -6.84210397760805], [5.006435002993213, -6.801055497538841], [5.4231591137305575, -6.535669296187095], [6.718224305995451, -6.343864689348279], [6.644882620251184, -6.623788309643334], [7.175993865866409, -6.785338014146947], [7.280220573454827, -6.275521507062111], [8.730435736731517, -6.208017894193431], [9.644119333648673, -6.326580323207856], [9.65669232536947, -7.790242863056315], [8.908196935688032, -7.333320758487551], [7.770907824800219, -7.142744457990316], [6.119914114822029, -7.813032125577482], [6.4442881807649535, -7.010784351273119], [5.827020035547118, -7.15378414889695], [5.5438383572909755, -7.795758657938674], [4.6624262868360855, -7.979419029844612], [4.126247709498728, -7.418172867442533], [3.7934642210449314, -7.986659423714846], [3.2839552277871658, -7.74479148855114], [2.3442497883309192, -7.941898150982489], [1.8985506745408078, -7.763486053031345], [0.09616460458049247, -7.990911072597328]]

# import matplotlib.pyplot as plt
# x, y = TSP(PONTOS)

# plt.plot(x,y)
# plt.show()
