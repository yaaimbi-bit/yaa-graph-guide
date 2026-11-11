# YAAGRAFGIDE20

Главный источник правды для AI и команды `yaa-graph-guide`: брендовые правила,
токены, компоненты, миграционный слой и структура этого репозитория.

## Сведения о сборке

- Режим: резервная внутренняя сборка без Node/npm.
- `node` и `npx` отсутствуют, поэтому `codegraph` не запускался.
- Карта ниже собрана прямым чтением tracked-файлов; секреты и `.git` не включены.
- Точные PDF-значения и отсутствующие параметры находятся в `BRANDBOOK.md`.

## 1. Брендовые ограничения

- Primary: `#00E67E`; bright: `#00FF8C`; secondary: `#444FC5`.
- Dark background: `#0E0E0E`; light background: `#FFFFFF`.
- Текст на зелёном: `#0E0E0E`.
- Текст зелёного цвета на светлом фоне: `#006B3F`; яркий `#00E67E` там не использовать.
- Heading role: фактический `Druck Cyrillic Heavy` из `fonts/druk/drukcyr-heavy.ttf`;
  в брендбуке роль названа `Druck Wide`. Файл опубликован по решению владельца,
  веб-лицензия пока не подтверждена.
- Accent: локальный variable `Roboto Flex`; body: локальный variable `Inter Tight`.
- Логотип: `assets/brand/YAA_logo_color.svg` на тёмном фоне, `YAA_logo_black.svg`
  на светлом. Не искажать, не перерисовывать и не перекрашивать вручную.

## 2. Токены

Единственный CSS-источник — `tokens.css`. В нём находятся:

- semantic colors, contrast-safe `success-text` и text-on-color;
- dark/light surfaces, border scale и input/dropdown/nav surfaces;
- font families, role aliases `hero/h1/h2/lg/input/btn/body/sm/detail/label`,
  weights `400/500/600/700/800`;
- spacing `4/8/12/16/20/24/32px`;
- radii `4/8/10/14/20px` и pill;
- hard shadows, `--yaa-elev-1`, `--yaa-elev-2`, focus ring и motion;
- chart palette `--yaa-chart-1` … `--yaa-chart-8`;
- product accents `hub/vanga/simmy/graph/map` и artist tiers.

`themes/dark.css` и `themes/light.css` переопределяют только тему. В светлой теме
`--yaa-color-primary-text` равен `#006B3F`, в тёмной — `#00E67E`.

## 3. Компоненты и паттерны

`components/components.css` — framework-agnostic слой:

```text
Card · Button · TextInput · Select · Badge · Chip · SignalCell · DataBar · Callout
Tabs · KPI · Table · Chart/Legend · Tooltip · Dropdown
```

Все интерактивные классы имеют `focus-visible`; Chip поддерживает
`.yaa-chip--active` и `[aria-pressed="true"]`; Callout имеет info/success/warning/error.
API-таблица старых React-пропсов → новых классов находится в `components/README.md`.

## 4. Tailwind и миграция

- `dashboard-theme.css` — основной способ для Tailwind v4: `@theme` связывает
  `gray-*`, `indigo-*`, `emerald-*`, `green-*` с токенами без `!important`.
- `dashboard-migration.css` — scoped fallback для уже собранной разметки
  `.yaa-dashboard`; покрывает обычные utility и `dark:bg-*`, `dark:text-*`,
  `dark:border-*` селекторы.
- `migration-guide.md` фиксирует источник каждого решения, намеренно снятые
  паттерны и порядок переноса одного дашборда.

Glow, blur, gradient text и radial green background из старой системы намеренно
не перенесены: новая система использует плоские поверхности и hard shadow.
`Roboto Serif` удалён из публичного репозитория как небрендовый и тяжёлый;
`Press Start 2P` оставлен только необязательным токеном без файла.

## 5. Карта репозитория

```text
.
├── AGENTS.md
├── BRANDBOOK.md
├── YAAGRAFGIDE20.md
├── README.md
├── migration-guide.md
├── tokens.css
├── themes/
│   ├── dark.css
│   └── light.css
├── dashboard-theme.css
├── dashboard-migration.css
├── components/
│   ├── components.css
│   └── README.md
├── storybook/
│   ├── index.html
│   └── README.md
├── assets/brand/
│   ├── YAA_logo_black.svg
│   └── YAA_logo_color.svg
├── fonts/
│   ├── Roboto_Flex/{OFL.txt,README.txt,*.ttf}
│   ├── inter/{OFL.txt,InterTight-Thin.ttf,InterTight.ttf}
│   └── druk/drukcyr-heavy.ttf
└── .agents/skills/yaa-graph-guide/
    ├── SKILL.md
    └── agents/openai.yaml
```

## 6. Рабочий поток

```text
tokens.css ─┬─> themes/*.css ───────────────┐
            ├─> components/components.css  ├─> storybook/index.html
            ├─> dashboard-theme.css        ├─> dashboard consumer
            └─> dashboard-migration.css ───┘

BRANDBOOK.md + tracked structure ──> YAAGRAFGIDE20.md
```

Перед кодом или UI review агент обязан прочитать этот файл целиком. Перед
публикацией проверить существование всех `url()`-ассетов, dark/light preview,
контраст и состояния компонентов. Не добавлять локальные HEX в компоненты,
если уже есть соответствующий токен.
