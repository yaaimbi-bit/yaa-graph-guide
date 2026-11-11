# YAA component preview

Эта папка содержит framework-agnostic preview для быстрой проверки компонентов до подключения настоящего Storybook runtime.

Открой index.html в браузере и переключай тему кнопкой в верхней части страницы.

## Story matrix

Каждый интерактивный компонент должен быть проверен в состояниях:

- default;
- hover;
- active;
- focus-visible;
- disabled;
- loading;
- invalid/error, если состояние применимо.

## Подключение в Storybook

1. Импортируй ../tokens.css.
2. Импортируй ../components/components.css.
3. Для dashboard stories импортируй ../dashboard-migration.css.
4. Перенеси markup из index.html в stories выбранного фреймворка.
5. Сохрани реальные данные дашборда и меняй только визуальный слой.
