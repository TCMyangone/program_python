class GameStars():
    '''记录游戏信息'''

    def __init__(self,ai_settings):
        '''初始化统计信息'''
        # 在任何情况下都不应该重置最高分
        with open (r'high_score.txt') as fl:
            sc = fl.read()
            self.high_score = int(sc)
        self.ai_settings = ai_settings
        self.reset_stars()
        # 游戏刚启动时处于非活动状态
        self.game_active = False

    def reset_stars(self):
        '''初始化游戏中可能变化的信息'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1