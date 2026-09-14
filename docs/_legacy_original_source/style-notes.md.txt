# Style Notes and Guidelines


## Introduction

This document outlines the **style notes and guidelines** for the Capybara Framework documentation.

All future editions should respect these choices unless explicitly updated in a new edition's "Style Notes and Guidelines" section.


## Color Palette

**Sepia Base Colors**

<table style="margin-bottom:1em;padding-bottom:1em;" cellpadding=5 cellspacing=5>
    <tr><td style="background-color:#9F5A2C;">#9F5A2C</td><td>primary sepia tone</td></tr>
    <tr><td style="background-color:#77390A;color:#FFFFFF;">#77390A</td><td>heading color</td></tr>
    <tr><td style="background-color:#DAC4B0;">#DAC4B0</td><td>light background / neutral</td></tr>
    <tr><td style="background-color:#C4A48A;">#C4A48A</td><td>accent / secondary background</td></tr>
</table>

**Blue Accent Colors**

<table style="margin-bottom:1em;padding-bottom:1em;" cellpadding=5 cellspacing=5>
    <tr><td style="background-color:#39BBFF;">#39BBFF</td><td>hyperlink / callout highlight</td></tr>
    <tr><td style="background-color:#277DD1;color:#FFFFFF;">#277DD1</td><td>secondary hyperlink / buttons</td></tr>
    <tr><td style="background-color:#0C61B9;color:#FFFFFF;">#0C61B9</td><td>tertiary accent</td></tr>
    <tr><td style="background-color:#00356B;color:#FFFFFF;">#00356B</td><td>deep accent / headers if needed</td></tr>
</table><br/>


## Headings

- All headings should use `#77390A`.
- In markdown, indicate headings with `# ` for top-level (`h1`), `## ` for second-level (`h2`), `### ` for third-level (`h3`).  
- In RST files, underscore headings with `=` for top-level (`h1`), `-` for second-level (`h2`), `~` for third-level (`h3`).  
- Keep headings clear and descriptive.

Example:

```
# Section Title

## Subsection Title

### Sub-subsection Title
```


## Text and Typography

- **Fonts:** The Original Edition uses the free and open-source fonts <em>Source Sans 3</em> and <em>Source Code Pro</em>.
- **Body text:** Dark brown or black, high contrast against light sepia backgrounds (`#DAC4B0` or `#C4A48A`).  
- **Links:** Use `#39BBFF` for standard links; hover states can be `#277DD1`.  
- **Emphasis:** Italics or bold as needed, but avoid excessive styling.


## Lists

- Use bullets for unordered lists (`-` or `*`), numbers for ordered lists (`1.`).  
- Nested lists are indented by **3 spaces** per level.  

Examples:
```
- First item
- - Nested item
- Second item
```


## Callouts / Notes

```
<div class="callout callout-default"><img src="/en/latest/_images/symbol-arrow.png" class="callout-icon"><span class="callout-title">Default Callout</span>
<strong>Note:</strong> This is a default callout.
</div>
```
<div class="callout callout-default"><img src="/en/latest/_images/symbol-arrow.png" class="callout-icon"><span class="callout-title">Default Callout</span>
<strong>Note:</strong> This is a default callout.
</div>

```
<div class="callout callout-tip"><img src="/en/latest/_images/symbol-lightbulb.png" class="callout-icon"><span class="callout-title">Tip Callout</span>
<strong>Note:</strong> This is a tip callout.
</div>
```
<div class="callout callout-tip"><img src="/en/latest/_images/symbol-lightbulb.png" class="callout-icon"><span class="callout-title">Tip Callout</span>
<strong>Note:</strong> This is a tip callout.
</div>

```
<div class="callout callout-check"><img src="/en/latest/_images/symbol-checkmark2.png" class="callout-icon"><span class="callout-title">Check Callout</span>
<strong>Note:</strong> This is a check callout.
</div>
```
<div class="callout callout-check"><img src="/en/latest/_images/symbol-checkmark2.png" class="callout-icon"><span class="callout-title">Check Callout</span>
<strong>Note:</strong> This is a check callout.
</div>

```
<div class="callout callout-info"><img src="/en/latest/_images/symbol-information.png" class="callout-icon"><span class="callout-title">Info Callout</span>
<strong>Note:</strong> This is an info callout.
</div>
```
<div class="callout callout-info"><img src="/en/latest/_images/symbol-information.png" class="callout-icon"><span class="callout-title">Info Callout</span>
<strong>Note:</strong> This is an info callout.
</div>

```
<div class="callout callout-warning"><img src="/en/latest/_images/symbol-exclamation.png" class="callout-icon"><span class="callout-title">Warning Callout</span>
<strong>Note:</strong> This is a warning callout.
</div>
```
<div class="callout callout-warning"><img src="/en/latest/_images/symbol-exclamation.png" class="callout-icon"><span class="callout-title">Warning Callout</span>
<strong>Note:</strong> This is a warning callout.
</div>

```
<div class="callout callout-important"><img src="/en/latest/_images/symbol-important.png" class="callout-icon"><span class="callout-title">Important Callout</span>
<strong>Note:</strong> This is an important callout.
</div>
```
<div class="callout callout-important"><img src="/en/latest/_images/symbol-important.png" class="callout-icon"><span class="callout-title">Important Callout</span>
<strong>Note:</strong> This is an important callout.
</div>

```
<div class="callout callout-technicalnote"><img src="/en/latest/_images/symbol-technicalnote.png" class="callout-icon"><span class="callout-title">Technical Note Callout</span>
<strong>Note:</strong> This is a technical note callout.
</div>
```
<div class="callout callout-technicalnote"><img src="/en/latest/_images/symbol-technicalnote.png" class="callout-icon"><span class="callout-title">Technical Note Callout</span>
<strong>Note:</strong> This is a technical note callout.
</div>

```
<div class="callout callout-bonusinfo"><img src="/en/latest/_images/symbol-bonusinfo.png" class="callout-icon"><span class="callout-title">Bonus Info Callout</span>
<strong>Note:</strong> This is a bonus info callout.
</div>
```
<div class="callout callout-bonusinfo"><img src="/en/latest/_images/symbol-bonusinfo.png" class="callout-icon"><span class="callout-title">Bonus Info Callout</span>
<strong>Note:</strong> This is a bonus info callout.
</div>

```
<div class="callout callout-questionbubble"><img src="/en/latest/_images/symbol-questionbubble.png" class="callout-icon"><span class="callout-title">Question Bubble Callout</span>
<strong>Note:</strong> This is a question bubble info callout.
</div>
```
<div class="callout callout-questionbubble"><img src="/en/latest/_images/symbol-questionbubble.png" class="callout-icon"><span class="callout-title">Question Bubble Callout</span>
<strong>Note:</strong> This is a question bubble info callout.
</div>

```
<div class="callout callout-ontarget"><img src="/en/latest/_images/symbol-target.png" class="callout-icon"><span class="callout-title">On Target Callout</span>
<strong>Note:</strong> This is an on target callout.
</div>
```
<div class="callout callout-ontarget"><img src="/en/latest/_images/symbol-target.png" class="callout-icon"><span class="callout-title">On Target Callout</span>
<strong>Note:</strong> This is an on target callout.
</div>

```
<div class="callout callout-screenshot"><img src="/en/latest/_images/symbol-screenshot.png" class="callout-icon"><span class="callout-title">Screenshot Callout</span>
<strong>Note:</strong> This is a screenshot callout.
</div>
```
<div class="callout callout-screenshot"><img src="/en/latest/_images/symbol-screenshot.png" class="callout-icon"><span class="callout-title">Screenshot Callout</span>
<strong>Note:</strong> This is a screenshot callout.
</div>

```
<div class="callout callout-quotation"><img src="/en/latest/_images/symbol-quotation2.png" class="callout-icon"><span class="callout-title">Quotation Callout</span>
<strong>Note:</strong> This is a quotation callout.
</div>
```
<div class="callout callout-quotation"><img src="/en/latest/_images/symbol-quotation2.png" class="callout-icon"><span class="callout-title">Quotation Callout</span>
<strong>Note:</strong> This is a quotation callout.
</div>

```
<div class="callout callout-closerlook"><img src="/en/latest/_images/symbol-look.png" class="callout-icon"><span class="callout-title">Closer Look Callout</span>
<strong>Note:</strong> This is a closer look callout.
</div>
```
<div class="callout callout-closerlook"><img src="/en/latest/_images/symbol-look.png" class="callout-icon"><span class="callout-title">Closer Look Callout</span>
<strong>Note:</strong> This is a closer look callout.
</div>

```
<div class="callout callout-comingsoon"><img src="/en/latest/_images/symbol-comingsoon2.png" class="callout-icon"><span class="callout-title">Coming Soon Callout</span>
<strong>Note:</strong> This is a coming soon callout.
</div>
```
<div class="callout callout-comingsoon"><img src="/en/latest/_images/symbol-comingsoon2.png" class="callout-icon"><span class="callout-title">Coming Soon Callout</span>
<strong>Note:</strong> This is a coming soon callout.
</div>

```
<div class="callout callout-externallinks"><img src="/en/latest/_images/symbol-externallink2.png" class="callout-icon"><span class="callout-title">External Links Callout</span>
<strong>Note:</strong> This is an external links callout.
</div>
```
<div class="callout callout-externallinks"><img src="/en/latest/_images/symbol-externallink2.png" class="callout-icon"><span class="callout-title">External Links Callout</span>
<strong>Note:</strong> This is an external links callout.
</div>

```
<div class="callout callout-video"><img src="/en/latest/_images/symbol-youtube.png" class="callout-icon"><span class="callout-title">Video Callout</span>
<strong>Note:</strong> This is a video callout.
</div>
```
<div class="callout callout-video"><img src="/en/latest/_images/symbol-youtube.png" class="callout-icon"><span class="callout-title">Video Callout</span>
<strong>Note:</strong> This is a video callout.
</div>

```
<div class="callout code callout-code"><img src="/en/latest/_images/symbol-pythonlogo2.png" class="callout-icon"><span class="callout-title">Python Callout</span>
<strong>Note:</strong> This is a Python callout.
</div>
```
<div class="callout code callout-code"><img src="/en/latest/_images/symbol-pythonlogo2.png" class="callout-icon"><span class="callout-title">Python Callout</span>
<strong>Note:</strong> This is a Python callout.
</div>

```
<div class="callout code callout-code"><span class="callout-title">Other code-centric icons</span>
<img src="/en/latest/_images/symbol-commandline2.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-rest.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-api.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-servicenow.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-arcgisonline.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-arcgisindoors.png" class="callout-icon">
</div>
```
<div class="callout code callout-code"><span class="callout-title">Other code-centric icons</span>
<img src="/en/latest/_images/symbol-commandline2.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-rest.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-api.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-servicenow.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-arcgisonline.png" class="callout-icon">&nbsp;
<img src="/en/latest/_images/symbol-arcgisindoors.png" class="callout-icon">
</div>

## Images

- Prefer **high-resolution images** and consistent styling.  
- Backgrounds should not clash with sepia tones; transparent backgrounds are ideal.  
- File naming: lowercase, hyphen-separated (see File Naming Conventions).


## Branding Consistency

- Capybara logo should appear in the **top-left** of Read the Docs sidebar.  
- Edition info (name, version, tagline) should appear directly below the logo.  
- Color accents in headings, links, and callouts should match the defined palette.


## Supplemental Guidelines

- Maintain **semantic Markdown / RST** structure for headings, lists, and links.  
- Update the **Style Notes and Guidelines** section whenever a new edition makes a deliberate style change.  
- Preserve **edition metadata** and **author/copyright credit** when creating forks or new versions.

