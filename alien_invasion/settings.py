class Settings():
    '''储存游戏设置的类'''

    def initialize_dynamic_settings(self):
        '''初始化游戏的动态设置'''
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        # fleet_direction为1表示向又移，-1表示向左移动
        self.fleet_direction = 1
        # 外星人分数
        self.alien_points = 50
    
    def initialize_stop_settings(self):
        '''初始游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (37,37,54)
        # 飞船设置
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 44,216,251
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 20
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        

    def increase_speed(self):
            '''提高速度设置和外星人点数'''
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)

    def __init__(self):
        '''初始化游戏的动静态设置'''
        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_stop_settings()
        self.initialize_dynamic_settings()

        
        
        
