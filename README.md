Установи общий скил YAA Graph Guide на локальный компьютер.

Источник:
https://github.com/yaaimbi-bit/yaa-graph-guide

Нужно выполнить установку самостоятельно, без инструкций для ручного копирования.

1. Определи пользовательскую директорию скилов Codex.
2. Установи туда папку:

   yaa-graph-guide/

3. Внутри должны находиться:

   - `SKILL.md`
   - `agents/openai.yaml`

4. Источник файлов:

   `https://github.com/yaaimbi-bit/yaa-graph-guide/tree/main/.agents/skills/yaa-graph-guide`

5. Если доступна project-scoped установка, также скопируй скил в текущий проект:

   `.agents/skills/yaa-graph-guide/`

6. Проверь, что Codex видит скил с именем:

   `$yaa-graph-guide`

7. После установки проверь, что скил умеет читать:

   `YAAGRAFGIDE20.md`

   из репозитория:

   `https://github.com/yaaimbi-bit/yaa-graph-guide`

8. Не проси пользователя копировать файлы вручную. Выполни установку, проверку структуры и сообщи итог.

После установки скил должен автоматически применяться перед генерацией кода, изменением архитектуры или разработкой UI.


## Состав репозитория

- tokens.css — единый источник CSS-токенов.
- themes/light.css и themes/dark.css — темы.
- components/components.css — 9 framework-agnostic компонентов.
- components/README.md — варианты, состояния и правила доступности.
- storybook/index.html — статический preview для быстрой визуальной проверки.
- dashboard-migration.css — scoped-слой для переноса Tailwind-дашбордов.
- migration-guide.md — решения, источники и критерии миграции.
- YAAGRAFGIDE20.md — архитектурный и брендовый контекст.
- .agents/skills/yaa-graph-guide — скил Codex.

## Быстрый preview

Открой storybook/index.html в браузере. Переключатель темы показывает dark/light режимы, а preview содержит Card, Button, TextInput, Select, Badge, Chip, SignalCell, DataBar и Callout.

Для настоящего Storybook runtime подключи tokens.css, components/components.css и dashboard-migration.css к stories выбранного frontend-фреймворка.


## Font assets

The repository includes the supplied YAA font package under `fonts/`:

- `fonts/druk/drukcyr-heavy.ttf` — primary display font, `Druck Cyrillic Heavy`;
- `fonts/Roboto_Flex/` — variable Roboto Flex and license files;
- `fonts/inter/InterTight-Thin.ttf` — supplied Inter Tight Thin;
- `fonts/Roboto_Serif/` — variable and static Roboto Serif family.

The preview uses Druck Cyrillic Heavy for the main heading and Roboto Flex for secondary headings and metrics.
