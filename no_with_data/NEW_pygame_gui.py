import pygame
import pygame_gui

SIZE = WIDTH, HEIGHT = 800, 600


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    background = pygame.Surface(SIZE)
    color = 'white'
    screen.fill(color)
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager(SIZE)
    switch = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 275), (100, 50)),
        text='switch',
        manager=manager
    )
    red = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((120, 475), (100, 50)),
        text='red', manager=manager
    )
    green = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 475), (100, 50)),
        text='green', manager=manager
    )
    blue = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((580, 475), (100, 50)),
        text='blue', manager=manager
    )
    difficulty = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['Easy', 'Medium', 'Hard'], starting_option='Easy',
        relative_rect=pygame.Rect((350, 150), (100, 25)), manager=manager
    )
    entry = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((350, 100), (100, 25)), manager=manager
    )
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirmation_dialog = pygame_gui.windows.UIConfirmationDialog(
                    rect=pygame.Rect((250, 200), (300, 200)), manager=manager,
                    window_title='Подтвердите действие',
                    action_long_desc="Вы уверенны, что хотите выйти?",
                    action_short_name='OK',
                    blocking=True
                )
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_CONFIRMATION_DIALOG_CONFIRMED:
                    running = False
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    print("name:", event.text)
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    print("difficulty:", event.text)
                if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                    if event.ui_element == red:
                        color = 'red'
                        background.fill(color)
                    if event.ui_element == green:
                        color = 'green'
                        background.fill(color)
                    if event.ui_element == blue:
                        color = 'blue'
                        background.fill(color)
                if event.user_type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                    if event.ui_element in [red, green, blue]:
                        color = 'black'
                        background.fill(color)
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == switch:
                        if color == 'black':
                            color = 'white'
                        else:
                            color = 'black'
                        background.fill(color)
            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(background, (0, 0))
        manager.draw_ui(screen)
        pygame.display.update()
    pygame.display.quit()


if __name__ == '__main__':
    main()
