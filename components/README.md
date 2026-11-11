# YAA components

Это framework-agnostic слой компонентов для миграции дашбордов. Он использует tokens.css и рассчитан на перенос в React, Vue, Streamlit или существующую Tailwind-разметку.

## Компоненты v1

| Компонент | Классы | Варианты и состояния |
|---|---|---|
| Card | yaa-card | default, interactive |
| Button | yaa-button | primary, secondary, ghost, sm, md, lg, disabled, loading |
| TextInput | yaa-input | default, invalid, focus |
| Select | yaa-select | default, invalid, focus |
| Badge | yaa-badge | success, warning, error, info |
| Chip | yaa-chip | default, hover, focus |
| SignalCell | yaa-signal-cell | success, warning, error, info |
| DataBar | yaa-data-bar | primary, secondary |
| Callout | yaa-callout | info, success, warning, error |
| Tabs | yaa-tabs, yaa-tab | default, selected, focus |
| KPI | yaa-kpi | value, positive/negative delta |
| Table | yaa-table-wrap, yaa-table | header, row hover, responsive overflow |
| Chart | yaa-chart, yaa-chart__legend | 8 chart colors, legend |
| Tooltip | yaa-tooltip | surface, border, elevation |
| Dropdown | yaa-dropdown | open, selected item |

## Соответствие старой React-системе

Статический пакет не меняет данные и не требует React runtime. При переносе старых
компонентов оставляй их публичные пропсы, а класс выбирай по этой таблице:

| Старый компонент / prop | Новый класс / атрибут |
|---|---|
| `Button variant="primary"` | `.yaa-button.yaa-button--primary` |
| `Button variant="ghost"` | `.yaa-button.yaa-button--ghost` |
| `TextInput` | `.yaa-input` |
| `Select options` | `.yaa-select` |
| `Badge tone="green|amber|orange"` | `.yaa-badge--success|warning|error` |
| `Chip onClick` | `.yaa-chip` + `role="button"`; active: `[aria-pressed="true"]` |
| `Card title` | `.yaa-card`; title: `.yaa-label` |
| `Callout tone="warning|error"` | `.yaa-callout--warning|error`; info: `.yaa-callout--info` |
| `SignalCell label/value` | `.yaa-signal-cell` + semantic modifier |
| `DataBar fill/value` | `.yaa-data-bar` + `.yaa-data-bar__value[style="width: …"]` |

Для новых экранов доступны также `.yaa-tabs`, `.yaa-kpi`, `.yaa-table`, `.yaa-chart`,
`.yaa-tooltip` и `.yaa-dropdown`.

## Правила

- Используй CSS custom properties из tokens.css, а не локальные HEX-значения.
- Для текста на основном зелёном используй --yaa-text-on-primary: #0E0E0E.
- Все интерактивные элементы должны иметь focus-visible.
- Disabled, loading и invalid нельзя имитировать только снижением opacity.
- Для новых вариантов сначала добавляй токен, затем компонентный класс.
- Если компонент переносится в Storybook, его story должна показывать default, hover, active, focus, disabled и loading, где это применимо.
