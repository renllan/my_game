import pygame
# 标识是否退出循环
exitFlag = False
# 设置画面刷新的帧率，即1s内刷新几次
FPS = 30
# 初始化pygame
pygame.init()
# 设置窗口标题
pygame.display.set_caption("pygame文字绘制教程")
# 设置窗口大小
surface = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)
# 设置icon
# icon = pygame.image.load('E:\AS-workspace\pygameTest\drawable\icon.png').convert_alpha()
# pygame.display.set_icon(icon)
# 获取游戏时钟
clock = pygame.time.Clock()
# 获取系统所有支持的文字名称
fonts = pygame.font.get_fonts()
print(fonts)
x = 10
y = 20
for f in fonts:
    f.get
    # 加载系统字体
    font = pygame.font.SysFont(f, 20)
    text = 'you crashed'
    # 设置是否加粗
    font.bold = True
    # 设置是否倾斜
    font.italic = True
    # 设置是否加下划线
    font.underline = True
    # 绘制文字到一个的Surface中并返回
    textSurface = font.render(text, True, (255, 221, 85))
    # 绘制前先获取文本的宽高
    width, height = font.size(text)
    # 绘制到显示器的surface上
    surface.blit(textSurface, (x, y))
    x += width + 20
    if x > 1800:
        y += 50
        x = 10
# 更新绘制到屏幕上
pygame.display.update()
while not exitFlag:
    clock.tick(FPS)
    for event in pygame.event.get():
        # 点击关闭
        if event.type == pygame.QUIT:
            exitFlag = True


