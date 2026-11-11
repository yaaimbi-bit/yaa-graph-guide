# YAA component preview

Эта папка содержит framework-agnostic preview для быстрой проверки компонентов и
Foundations до подключения настоящего Storybook runtime.

Открой `index.html` в браузере и переключай тему кнопкой в верхней части страницы.
Для автоматического снимка можно открыть `index.html?theme=dark` или
`index.html?theme=light`.

## Story matrix

Каждый интерактивный компонент должен быть проверен в состояниях:

- default;
- hover;
- active;
- focus-visible;
- disabled;
- loading;
- invalid/error, если состояние применимо.

Preview также показывает Colors, Typography, Logo, Tabs, KPI, Table, Chart legend,
Tooltip и Dropdown — паттерны, которых не было в старом статичном слое.

## Подключение в Storybook

1. Импортируй ../tokens.css.
2. Импортируй ../components/components.css.
3. Для новых Tailwind v4 dashboard stories импортируй ../dashboard-theme.css.
4. Для legacy utility-классов дополнительно импортируй ../dashboard-migration.css.
5. Перенеси markup из index.html в stories выбранного фреймворка.
6. Сохрани реальные данные дашборда и меняй только визуальный слой.
