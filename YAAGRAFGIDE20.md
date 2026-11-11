# YAAGRAFGIDE20

Единый граф-гайд проекта: брендовые правила и архитектура кода.

## Сведения о сборке

- Режим: резервная внутренняя сборка.
- Причина: `node` и `npx` отсутствуют в окружении.
- Стандартная команда `npx -y @colbymchenry/codegraph build --output ./docs/CODE_STRUCT.md` не запускалась.
- Структура собрана прямым сканированием файлов проекта.
- Просканировано: `108` файлов.
- Секретные значения из `.env` не включены.
- Исключены из сканирования: `.git`, `.venv`, `node_modules`, `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.ruff_cache`.

---

# BRANDBOOK DESIGN TOKENS

Источник: `Brand YAA.pdf`, 25 страниц, размер страницы `1920 × 1080 pt`.

Значения, которых нет в PDF, помечены как `Не указано`. Визуальные выводы не заменяют отсутствующие числовые токены.

## 1. Цветовая палитра

### Цвета, указанные в PDF

| Токен | HEX | RGB | Использование |
|---|---|---|---|
| `--color-white` | `#FFFFFF` | `255, 255, 255` | Светлый фон, текст на тёмном фоне |
| `--color-black` | `#0E0E0E` | `14, 14, 14` | Тёмный фон, текст на светлом фоне |
| `--color-green` | `#00E67E` | `0, 230, 126` | Основной фирменный зелёный |
| `--color-green-bright` | `#00FF8C` | `0, 255, 140` | Дополнительный яркий зелёный |
| `--color-blue` | `#444FC5` | `65, 79, 197` | Фирменный синий |

### Семантические роли

PDF не присваивает цветам семантические имена `Primary`, `Secondary`, `Success` и `Error`. Следующее соответствие является рабочей интерпретацией для фронтенда:

| Семантическая роль | Значение | Статус |
|---|---|---|
| `Primary` | `#00E67E` | Рекомендуемое соответствие по визуальному использованию |
| `Secondary` | `#444FC5` | Рекомендуемое соответствие по визуальному использованию |
| `Background dark` | `#0E0E0E` | Указано в PDF |
| `Background light` | `#FFFFFF` | Указано в PDF |
| `Text on dark` | `#FFFFFF` | Указано в PDF |
| `Text on light` | `#0E0E0E` | Указано в PDF |
| `Success` | Не указано | Отдельный success-цвет отсутствует |
| `Error` | Не указано | Отдельный error-цвет отсутствует |

Красный цвет в PDF используется в примерах недопустимой перекраски логотипа и не определён как цвет ошибки.

```css
:root {
  --color-white: #FFFFFF;
  --color-black: #0E0E0E;
  --color-green: #00E67E;
  --color-green-bright: #00FF8C;
  --color-blue: #444FC5;

  --color-primary: var(--color-green);
  --color-secondary: var(--color-blue);
  --color-background-dark: var(--color-black);
  --color-background-light: var(--color-white);
  --color-text-on-dark: var(--color-white);
  --color-text-on-light: var(--color-black);
}
```

## 2. Типографика

### Шрифтовые семейства

| Роль | Шрифт | `font-size` | `line-height` | `font-weight` | `letter-spacing` |
|---|---|---:|---:|---:|---:|
| Акцентный заголовочный шрифт | `Roboto Flex` | Не указано | `75–80%` | Не указано | `-1% до -2%` |
| Основной заголовочный шрифт | `Druck Wide` | Не указано | Не указано | Не указано | `-1% до -2%` |
| Шрифт для наборного текста | `Inter Tight Regular` | Не указано | Не указано | `Regular`; числовое значение не указано | `-1% до -2%` |

### CSS-интерпретация указанных диапазонов

PDF задаёт трекинг в процентах. Для CSS допустимая рабочая форма требует перевода в относительные единицы:

```css
:root {
  --font-family-accent: "Roboto Flex", sans-serif;
  --font-family-heading: "Druck Wide", sans-serif;
  --font-family-body: "Inter Tight", sans-serif;

  --letter-spacing-brand-min: -0.01em;
  --letter-spacing-brand-max: -0.02em;

  --line-height-accent-min: 0.75;
  --line-height-accent-max: 0.8;
}
```

Перевод диапазона в `em` и unitless `line-height` — техническая CSS-интерпретация; точные CSS-значения в PDF не приведены.

### Иерархия заголовков

Отдельные параметры для `H1–H6` в PDF отсутствуют.

| Элемент | Шрифт | `font-size` | `line-height` | `font-weight` |
|---|---|---:|---:|---:|
| `H1` | Не указано | Не указано | Не указано | Не указано |
| `H2` | Не указано | Не указано | Не указано | Не указано |
| `H3` | Не указано | Не указано | Не указано | Не указано |
| `H4` | Не указано | Не указано | Не указано | Не указано |
| `H5` | Не указано | Не указано | Не указано | Не указано |
| `H6` | Не указано | Не указано | Не указано | Не указано |
| Body | `Inter Tight Regular` | Не указано | Не указано | `Regular` |

## 3. Сетка и отступы

| Параметр | Значение |
|---|---:|
| Максимальная ширина контейнера | Не указано |
| Минимальная ширина контейнера | Не указано |
| Количество колонок | Не указано |
| Размер gutter | Не указано |
| `padding` | Не указано |
| `margin` | Не указано |
| Базовый spacing-токен | Не указано |
| Breakpoints | Не указано |
| Мобильный контейнер | Не указано |
| Desktop-контейнер | Не указано |

Размер страниц PDF `1920 × 1080 pt` является размером макетов брендбука, а не стандартом web-контейнера.

## 4. Компоненты

### Кнопки

В PDF показаны состояния `Static`, `Hover` и `Click`.

#### Основная кнопка

| Параметр | Значение |
|---|---|
| Фон | `#444FC5` или `#00E67E` в зависимости от контекста |
| Текст | `#FFFFFF` |
| Форма | Прямоугольная кнопка со скруглёнными углами |
| Акцент | Жёсткая смещённая цветная тень или контур |
| `border-radius` | Числовое значение не указано |
| `padding` | Не указано |
| `height` | Не указано |
| `font-size` | Не указано |
| `font-weight` | Не указано |
| `box-shadow` | Числовые параметры не указаны |

#### Вторичная кнопка

| Параметр | Значение |
|---|---|
| Фон | Прозрачный или фон контейнера |
| Текст | `#444FC5`, `#00E67E` или `#FFFFFF` в зависимости от фона |
| Форма | Текстовая или контурная кнопка |
| Акцент | Цветная смещённая линия или тень |
| `border-radius` | Числовое значение не указано |
| `padding` | Не указано |
| `height` | Не указано |
| `font-size` | Не указано |
| `font-weight` | Не указано |

### Скругления

Кнопки визуально имеют мягкое скругление углов, но точный радиус в пикселях или относительных единицах не задан.

```css
/* Точное значение в Brand YAA.pdf отсутствует */
border-radius: undefined;
```

### Тени

В примерах кнопок используется плоская жёсткая тень со смещением по горизонтали и вертикали. Числовые значения `offset-x`, `offset-y`, `blur-radius`, `spread-radius` и прозрачности не указаны.

### Иконки и графические элементы

| Параметр | Значение |
|---|---|
| Отдельная система интерфейсных иконок | Не описана |
| Размер иконок | Не указан |
| Толщина линий | Не указана |
| `stroke-linecap` | Не указано |
| `stroke-linejoin` | Не указано |
| Отступы вокруг иконок | Не указаны |
| Фирменные графические элементы | Щупальца, петли, органические контуры и логотип YAA |
| Правило для логотипа | Использовать оригинальную форму без искажения и недопустимой перекраски |

## 5. Параметры, отсутствующие в PDF

- точные размеры `H1–H6`;
- числовые значения `font-weight`;
- `line-height` для основных заголовков и body-текста;
- размеры web-контейнеров;
- сетка и breakpoints;
- spacing scale;
- числовые значения `border-radius`;
- точные параметры `box-shadow`;
- размеры иконок;
- отдельные токены `Success` и `Error`;
- состояния `Disabled`, `Focus` и `Loading`.

---

## 6. Карта репозитория

### Дерево верхнего уровня

```text
.
├── AGENTS.md
├── BRANDBOOK.md
├── YAAGRAFGIDE20.md
├── config.py
├── dashboard.py
├── scheduler.py
├── schema.sql
├── requirements.txt
├── db/
├── instagram-mcp/
├── pachca-mcp/
├── telegram-bot-mcp/
├── telegram-mcp/
├── tochka/
├── .agents/
├── .claude/
├── .env.example
├── .gitignore
└── yaa-facebook-cover-en.png
```

### Основное Python-приложение

```text
config.py
├── os
└── dotenv

dashboard.py
├── streamlit
├── pandas
├── pyarrow
├── plotly.express
├── db.queries
└── scheduler

scheduler.py
├── apscheduler.schedulers.blocking
├── apscheduler.triggers.interval
├── config
├── tochka.client
└── db.queries

db/
├── __init__.py
├── connection.py
│   ├── requests
│   └── config
└── queries.py
    ├── db.connection
    ├── logging
    ├── datetime
    └── typing

tochka/
├── __init__.py
└── client.py
    ├── requests
    ├── config
    ├── logging
    ├── datetime
    ├── typing
    └── time

schema.sql
└── SQL-схема базы данных
```

### MCP-сервисы

```text
instagram-mcp/
├── main.py
│   ├── httpx
│   ├── dotenv
│   └── mcp.server.fastmcp
├── README.md
├── .env.example
└── .env

pachca-mcp/
├── main.py
│   ├── httpx
│   ├── dotenv
│   └── mcp.server.fastmcp
├── README.md
├── requirements.txt
├── .env.example
└── .env

telegram-bot-mcp/
├── main.py
│   ├── httpx
│   ├── dotenv
│   └── mcp.server.fastmcp
├── README.md
├── .env.example
└── .env
```

### Telegram MCP

```text
telegram-mcp/
├── main.py
│   ├── telegram_mcp.install_guard
│   ├── telegram_mcp.runtime
│   ├── telegram_mcp.runner
│   └── telegram_mcp.tools
├── sanitize.py
├── session_string_generator.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── poetry.lock
├── uv.lock
├── Dockerfile
├── docker-compose.yml
├── claude_desktop_config.json
├── .github/workflows/
│   ├── docker-build.yml
│   ├── python-lint-format.yml
│   └── tests.yml
├── telegram_mcp/
│   ├── __init__.py
│   ├── client_identity.py
│   ├── contact_sheet.py
│   ├── install_guard.py
│   ├── photo_source.py
│   ├── runner.py
│   ├── runtime.py
│   ├── singleton.py
│   ├── transcription.py
│   └── tools/
│       ├── __init__.py
│       ├── accounts.py
│       ├── chats.py
│       ├── contacts.py
│       ├── events.py
│       ├── folders.py
│       ├── groups.py
│       ├── media.py
│       ├── messages.py
│       └── profile.py
├── tests/
│   ├── conftest.py
│   ├── test_aliases.py
│   ├── test_client_identity.py
│   ├── test_contact_sheet.py
│   ├── test_content_safeguards.py
│   ├── test_edit_chat_basic_group.py
│   ├── test_error_logging.py
│   ├── test_event_feed.py
│   ├── test_file_path_security.py
│   ├── test_flood_wait.py
│   ├── test_forum_topics.py
│   ├── test_forward_attribution.py
│   ├── test_forward_message_routing.py
│   ├── test_get_chat.py
│   ├── test_install_guard.py
│   ├── test_invite_to_group.py
│   ├── test_media_album.py
│   ├── test_media_download.py
│   ├── test_photo_source.py
│   ├── test_photo_tools.py
│   ├── test_profile_fields.py
│   ├── test_remove_user.py
│   ├── test_reply_quote.py
│   ├── test_rich_messages.py
│   ├── test_runner.py
│   ├── test_runtime.py
│   ├── test_sanitize.py
│   ├── test_schema_drift.py
│   ├── test_session_pool.py
│   ├── test_session_string_generator.py
│   ├── test_transcription.py
│   ├── test_validation.py
│   └── test_voice_transcripts.py
└── screenshots/
    ├── 1.png
    ├── 2.png
    └── 3.png
```

### Telegram MCP: связи модулей

```text
main.py
└── runner.py
    ├── install_guard.py
    ├── runtime.py
    ├── singleton.py
    └── tools/
        ├── accounts.py
        ├── chats.py
        ├── contacts.py
        ├── events.py
        ├── folders.py
        ├── groups.py
        ├── media.py
        ├── messages.py
        └── profile.py

runtime.py
├── Telethon
├── MCP FastMCP
├── SQLite
├── dotenv
├── python-json-logger
├── python-socks
├── sanitize.py
├── client_identity.py
└── singleton.py

transcription.py
├── Telegram runtime
├── Telethon
├── SQLite
└── transcripts table
```

### Тестовые зоны

- Алиасы, чаты, контакты и профили.
- Пересылка сообщений, цитаты и rich messages.
- Медиа, альбомы, фотографии и contact sheets.
- Форумные темы, группы, папки и события.
- Сессии, singleton, runtime и runner.
- Безопасность путей, safeguards и обработка ошибок.
- Транскрипция и голосовые сообщения.
- Валидация и контроль дрейфа схемы.

## 7. Ключевые архитектурные потоки

### Dashboard и планировщик

```text
dashboard.py
├── читает данные через db.queries
├── использует scheduler
└── визуализирует данные через Streamlit, pandas, PyArrow и Plotly

scheduler.py
├── запускает интервальные задачи APScheduler
├── обращается к Tochka API через tochka.client
└── использует db.queries для данных

db.queries
└── db.connection
    └── config.py
```

### MCP-сервисы HTTP

```text
instagram-mcp/main.py ──┐
pachca-mcp/main.py ──────┼──> httpx + dotenv + MCP FastMCP
telegram-bot-mcp/main.py ┘
```

### Правила работы агента

- Перед изменением кода читать этот файл целиком.
- UI-решения проверять по разделу `BRANDBOOK DESIGN TOKENS`.
- Архитектурные решения проверять по разделу `Карта репозитория`.
- Не считать отсутствующие в PDF значения заданными: `font-size`, точные отступы, `border-radius`, `box-shadow`, breakpoints и UI-состояния требуют отдельного решения.
- Не включать содержимое `.env` и другие секреты в документацию или код.


---

## 8. Рабочая дизайн-система v1

Подход основан на артефакте «Дашборды YAA до и после»: сравниваются одинаковые данные в старой и новой оболочке, а решения фиксируются с источником и статусом.

### Реализация

tokens.css
├── themes/
│   ├── dark.css
│   └── light.css
├── components/
│   ├── components.css
│   └── README.md
├── storybook/
│   ├── index.html
│   └── README.md
├── dashboard-migration.css
└── migration-guide.md

### Источник решений

- Точные брендовые значения берутся из Brand YAA.pdf.
- Продуктовые значения, которых нет в PDF, помечены как решения v1 в migration-guide.md.
- Реальные компоненты и состояния описываются в components/README.md и реализуются в components/components.css.
- Дашборд мигрируется через scoped-класс yaa-dashboard, чтобы не ломать остальное приложение.
- Бизнес-данные, формулы и идентификаторы при миграции не меняются.

### Утверждённые базовые токены

- Primary: #00E67E.
- Primary bright: #00FF8C.
- Secondary: #444FC5.
- Dark surface: #0E0E0E.
- Light surface: #FFFFFF.
- Text on primary: #0E0E0E.
- Warning: #FFD166.
- Error: #FF9871.
- Font heading: Druck Wide role with Archivo fallback; paid font files are excluded from this public repository.
- Font accent: Roboto Flex.
- Font body: Inter Tight с Inter fallback.
- Hard shadow: 4px 4px 0.
- Spacing: 4, 8, 12, 16, 20, 24, 32px.
- Radius: 4, 8, 10, 14, 20px.

### Проверка перед миграцией

1. Сверить реальные цифры до и после.
2. Проверить обе темы.
3. Проверить default, hover, active, focus-visible, disabled и loading.
4. Проверить контраст текста.
5. Убедиться, что локальные HEX-значения не обходят tokens.css.
6. Зафиксировать новые решения в migration-guide.md.
