import pygame
import win32api
import win32con
import win32gui

lenth=1920
high=1080
pygame.init()
#pygame.NOFRAME
screen = pygame.display.set_mode((lenth, high)) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (0, 0, 0)

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 40, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(fuchsia)  # Transparent background
    pygame.draw.rect(screen, dark_red, pygame.Rect(60, 80, 300, 60))
    pygame.draw.rect(screen, dark_red, pygame.Rect(1560, 80, 300, 60))
    pygame.draw.rect(screen, dark_red, pygame.Rect(1560, 940, 300, 60))
    pygame.draw.rect(screen, dark_red, pygame.Rect(60, 940, 300, 60))
    pygame.draw.rect(screen, dark_red, pygame.Rect(lenth/2-250, high/2-150, 60, 300))
    pygame.draw.rect(screen, dark_red, pygame.Rect(lenth/2+250, high/2-150, 60, 300))
    pygame.display.update()
