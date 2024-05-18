import random

class LaneManager:
    START_LEVEL = 0
    MAX_LEVEL = 10
    START_LANE = 6
    lane_number = START_LANE
    level = START_LEVEL
    ball = None
    results = {}

    def __init__(self):
        result_keys = [i for i in range(13)]
        for key in result_keys:
            self.results[key] = 0

    def has_ball(self):
        return self.ball != None

    def __reset(self):
        self.lane_number = self.START_LANE
        self.level = self.START_LEVEL
        self.ball = None

    def __score(self):
        self.results[self.lane_number] += 1
        self.__reset()

    def __end_level(self):
        self.level += 1
        if self.level == self.MAX_LEVEL:
            self.__score()

    def __ball_enters_lane_from_left(self, ball):
        ball.set_value(1)
        self.lane_number += 1

    def __ball_enters_lane_from_right(self, ball):
        ball.set_value(1)
        self.lane_number -= 1

    def add_ball_from_top(self, ball):
        ball.set_value(1)
        self.ball = ball

    def __bumper_hit(self):
        return random.randint(0,1)

    def __ball_goes_left(self):
        if self.ball.value == 0:
            self.__ball_enters_lane_from_right(self.ball)
        else:
            self.ball.value -= 1

    def __ball_goes_right(self):
        if self.ball.value == 2:
            self.__ball_enters_lane_from_left(self.ball)
        else:
            self.ball.value += 1

    def go(self):
        new_value = self.__bumper_hit()
        if new_value == 0:
            self.__ball_goes_left()
        if new_value == 1:
            self.__ball_goes_right()

        self.__end_level()

    def get_results(self):
        return self.results