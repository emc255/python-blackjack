import pygame

from card_elements import Deck


def testing():
    deck = Deck(2)
    print(len(deck.cards))
    for d in deck.cards:
        print(d.image)

    print(1 >= 1)


def table_test():
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    surface.fill((66, 123, 184))
    deck = Deck(1)
    image = pygame.transform.scale(pygame.image.load(deck.cards[12].image), (80, 100))
    image_x = 10
    image_y = 10

    # Blit the card onto the main surface

    surface.blit(image, (image_x, image_y))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_x -= .25
        if keys[pygame.K_RIGHT]:
            image_x += .25
        if keys[pygame.K_UP]:
            image_y -= .25
        if keys[pygame.K_DOWN]:
            image_y += .25

        # Blit the card onto the main surface at its updated position
        surface.fill((66, 123, 184))  # Fill the background with blue
        surface.blit(image, (image_x, image_y))

        # Flip the buffers to make the changes visible on the screen
        pygame.display.flip()


if __name__ == '__main__':
    testing()
    # table_test()
