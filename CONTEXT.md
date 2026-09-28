# athenaOS

Agentic Task Hosting & Embedded Natural-language Assistant desktop shell and distributed mission control system.

## Core Topology

**Host Shell**:
The desktop overlay and primary operating environment running on Fedora Linux, Windows, or macOS that executes autonomous agent workflows and OS automation tasks.
_Avoid_: Desktop app, main program

**Mission Control**:
A lightweight satellite interface running on edge devices (such as Raspberry Pi) that acts as an intelligent smart display, streaming status and relaying voice-driven task dispatches to the Host Shell.
_Avoid_: Client app, remote control, mini OS

**Computer-Use Automation**:
The subsystem where the agent directly interfaces with host operating system shells, GUIs, and terminal environments to execute multi-step user tasks.
_Avoid_: Screen scraping, macro execution

**Smart HUD**:
The compact, ambient floating status overlay that athenaOS collapses into when an agent is actively performing computer-use tasks on the host operating system.
_Avoid_: Minimized window, system tray popup

## Window Management & Staging

**Foreground Window**:
The single active modal window occupying primary screen focus at any given moment.
_Avoid_: Main window, active modal

**Stage Manager**:
The window lifecycle system that limits the desktop to a single foreground application and stages up to two recent background applications as interactive identity cards in the dock.
_Avoid_: Window switcher, task manager, alt-tab

**Staged App**:
A backgrounded application currently docked in one of the two active Stage Manager preview slots.
_Avoid_: Minimized app, suspended process

## Rendering & Graphics

**Blend2D Canvas**:
The JIT-compiled 2D vector graphics subsystem powering glassmorphic surfaces, dynamic Oklab theming, typography, and shadow effects across all supported platforms (macOS, Windows, Fedora Linux, Raspberry Pi).
_Avoid_: Cairo backend, Skia renderer

**Theme Context**:
The dynamic, APCA-compliant color synthesis engine that dynamically generates palettes and handles real-time perceptual color transitions.
_Avoid_: Style manager, CSS theme

**Font Resolver**:
The multi-tier typography pipeline that detects native OS font paths (Windows `Segoe UI`, macOS `SF Pro`, Linux `DejaVu`/`Inter`) and falls back gracefully to embedded font binaries.
_Avoid_: FreeType wrapper, font finder
