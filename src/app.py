
from lane_manager import LaneManager
from ball import Ball
from result_printer import ResultPrinter

balls = [Ball() for i in range(100000)]
lane_manager = LaneManager()

for ball in balls:
    lane_manager.add_ball_from_top(ball)
    while(lane_manager.has_ball()):
        lane_manager.go()

results = lane_manager.get_results()
printer = ResultPrinter()
printer.print_results(results)