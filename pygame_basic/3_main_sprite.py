import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/data_analysis/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/data_analysis/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴, rect : 사각형
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width)/ 2 # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면 세로 가장 아래에 위치

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 프로그램이 중단되지 않도록 계속 대기하는것, 사용자가 키보드나 마우스로 동작하는지 체크
        if event.type == pygame.QUIT: # 맨 위 오른쪽의 x버튼 누르면 창 닫기
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기!!! 계속 호출해야함

# pygame 종료
pygame.quit()