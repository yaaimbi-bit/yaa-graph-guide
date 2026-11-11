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

## Правила

- Используй CSS custom properties из tokens.css, а не локальные HEX-значения.
- Для текста на основном зелёном используй --yaa-text-on-primary: #0E0E0E.
- Все интерактивные элементы должны иметь focus-visible.
- Disabled, loading и invalid нельзя имитировать только снижением opacity.
- Для новых вариантов сначала добавляй токен, затем компонентный класс.
- Если компонент переносится в Storybook, его story должна показывать default, hover, active, focus, disabled и loading, где это применимо.
