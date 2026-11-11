# YAA Graph Guide

Единый framework-agnostic слой для YAA-дашбордов: токены, темы, компоненты,
Tailwind v4 bridge и статичный Foundation preview.

## Источник решений

- `BRANDBOOK.md` — точные значения из `Brand YAA.pdf`.
- `tokens.css` — единственный CSS-источник токенов.
- `migration-guide.md` — решения v1, происхождение и намеренно снятые паттерны.
- `storybook/index.html` — визуальная проверка dark/light без npm runtime.
- `YAAGRAFGIDE20.md` — главный контекст для AI и команды.

## Быстрый preview

Открой `storybook/index.html` в браузере. Переключатель показывает обе темы;
страница содержит Foundations, 9 базовых компонентов и новые dashboard-паттерны.
Для настоящего Storybook подключи `tokens.css`, `components/components.css`,
`dashboard-theme.css` и `dashboard-migration.css` к stories выбранного фреймворка.

## Структура

```text
tokens.css                 # цвета, типографика, spacing, радиусы, elevation
themes/{dark,light}.css    # theme overrides
components/components.css  # framework-agnostic primitives
components/README.md       # API mapping и accessibility rules
dashboard-theme.css        # Tailwind v4 @theme bridge
dashboard-migration.css    # scoped fallback для уже собранных utility-классов
storybook/index.html       # статичный dark/light preview
assets/brand/              # цветной и чёрный SVG-логотипы
fonts/                     # Roboto Flex, Inter Tight и опубликованный Druck
```

## Токены, которые добавлены из старой системы

| Группа | Токены |
|---|---|
| Графики | `--yaa-chart-1` … `--yaa-chart-8` |
| Продукты | `--yaa-accent-hub`, `vanga`, `simmy`, `graph`, `map` |
| Artist tier | `--yaa-tier-star`, `large`, `mid`, `club`, `micro` |
| Поверхности | `--yaa-surface-drop`, `input`, `input-focus`, `nav-bg` |
| Типографика | role aliases от `hero` 64px до `label` 11px; `black: 800` |
| Elevation | `--yaa-elev-1`, `--yaa-elev-2` |

Радиусы старой системы `12px/16px` нормализованы в v1 как `10px/14px` для
контролов и карточек. Glow, blur, gradient text и radial green background
намеренно не перенесены: новая система держится на плоских поверхностях и
жёсткой смещённой тени, чтобы бренд работал одинаково в обеих темах.

## Лицензия шрифтов

- `InterTight.ttf` — variable-файл для `400/500/600/700`, рядом лежит `fonts/inter/OFL.txt`.
- `Roboto Flex` — variable-файл и OFL в `fonts/Roboto_Flex/`.
- В брендбуке указана роль `Druck Wide`; в систему добавлен предоставленный
  `Druck Cyrillic Heavy` как фактический display-шрифт. Файл лежит в
  `fonts/druk/drukcyr-heavy.ttf` и подключается через `--yaa-font-heading`.
  Веб-лицензия файла пока не подтверждена: публикация сделана по прямому
  решению владельца проекта, коммерческое использование требует подтверждения.
- `Roboto Serif` не входит в брендбук и удалён из публичной системы осознанно;
  он не нужен токенам и весил около 23 МБ.
- `Press Start 2P` встречался в старом Cerebro как декоративный retro-акцент;
  оставлен только как необязательный `--yaa-font-retro`, без загрузки файла.

## Логотип

- В шапке: 36–40px; на титульном экране: 52–64px.
- Используй `assets/brand/YAA_logo_color.svg` на тёмном фоне и
  `assets/brand/YAA_logo_black.svg` на светлом.
- Сохраняй пропорции и clear space не меньше высоты знака по периметру.
- Для favicon подготовь 32px PNG/ICO и 180px touch icon из утверждённого SVG.
- В CSP-ограниченной среде встраивай готовый SVG/base64; не рисуй текстовый
  псевдологотип и не перекрашивай знак вручную.

## Статус раскатки

| Проект из прежнего README | Статус в этой системе |
|---|---|
| `yaa-events-dashboard` | готов слой; нужна live-проверка дашборда |
| `intickets-dashboard` | готов Tailwind bridge; нужна live-проверка |
| `yaa-fairytale-dashboard` | готов Tailwind bridge; нужна live-проверка |
| `yaa_kz_dasbhoard` | нужен smoke-test статичного подключения |
| `yaa-marketing-brief` | нужен smoke-test статичного подключения |
| остальные YAA-фронты | отдельная инвентаризация и rollout |

`Platinumlist` и `Chatpush` остаются вне области этой системы: это другой бренд.

## Миграция Tailwind v4

Для нового дашборда после `@import "tailwindcss"` подключи
`dashboard-theme.css`: он связывает `gray-*`, `indigo-*`, `emerald-*` и `green-*`
с токенами без `!important`. Для уже собранных обычных utility-классов добавь
`dashboard-migration.css` на корень `.yaa-dashboard`; он отдельно покрывает
`dark:bg-*`, `dark:text-*` и `dark:border-*`.

Зелёный `#00E67E` используется как поверхность/акцент. На светлой теме ссылки
и текст используют `--yaa-color-primary-text: #006B3F`, потому что яркий зелёный
на белом не проходит контраст для обычного текста. На зелёном фоне текст всегда
`--yaa-text-on-primary: #0E0E0E`.

## Контроль перед публикацией

- проверить dark и light preview;
- проверить default, hover, active, focus-visible, disabled, loading и invalid;
- убедиться, что каждый `url()` из `tokens.css` существует;
- проверить контраст текста и отсутствие локальных HEX в компонентах;
- сохранить данные, формулы и идентификаторы дашборда;
- только после визуального review разделить изменения на A/B/V и публиковать.
