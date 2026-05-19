---
title: Circuit Network Beginner Guide
description: Learn Factorio circuit network from scratch. Step-by-step guide with red-green wires, decider combinator, arithmetic combinator, and practical builds like SR latch and automated cracking.
date: 2026-05-19
tags: ["blueprints", "circuit-network"]
draft: false
---

I spent my first 200 hours in Factorio ignoring the circuit network entirely. Red and green wires sat in my inventory unused. Every base I built eventually deadlocked — belts backed up, oil refineries ground to a halt, and train intersections turned into parking lots. The circuit network looked intimidating, so I skipped it.

Turns out you only need three basic patterns to solve 90% of your circuit problems. I will walk through them from zero.

{{< callout "tip" >}}
**TL;DR:** Red wire and green wire are separate networks. A decider combinator outputs a signal when a condition is true. An arithmetic combinator does math on signals. Connect a storage tank to a pump with red wire, set the decider to "petroleum > 20000 output petroleum = 1", and you have automated cracking. That is it — 90% of circuit problems solved with this one trick.
{{< /callout >}}

{{< section "The Two Wires — What They Actually Do" >}}

Red wire and green wire are independent signal channels. Think of them as two separate data buses running through your factory.

A wire connects entities into a circuit network. Every entity on the same color wire can read signals from every other entity on that wire. Connect a power pole, and the network extends its reach.

{{< diagram "diagrams/circuit-wires.svg" "Red wire and green wire as two separate signal networks" "600" >}}

Wire colors do not mix by default. But you can combine them inside a combinator — a decider or arithmetic combinator reads from one or both colors and outputs to either color.

I use red wire for production logic (tank levels, belt contents, chest monitoring) and green wire for global signals (train schedules, logistics requests, base-wide alerts). Keeping them separate means a bug in one does not corrupt the other.

{{< callout "tip" >}}
If you want two entirely separate control systems, use red for one and green for the other. I use red for production logic and green for train control most playthroughs.
{{< /callout >}}

{{< section "Decider Combinator — The Smart Switch" >}}

The decider combinator is the most useful component in the entire circuit system. It checks a condition and outputs a signal if the condition is true.

**Input:** Signals from the connected network (red, green, or both)
**Condition:** Compare a signal to a value or another signal
**Output:** A signal of your choice (or the input signal itself)

Configuration example:
- Input: petroleum gas = 24000 (from a storage tank via red wire)
- Condition: petroleum > 20000
- Output: petroleum = 1

When petroleum exceeds 20000, the combinator outputs a single petroleum signal. Connect this output to a pump on the heavy oil to light oil cracking line, and you have built an automatic cracker.

You can compare any signal against any other signal too. Wire both storage tanks to the combinator and set "petroleum > heavy_oil". The combinator outputs when petroleum outpaces heavy oil. This handles refineries that skew production.

{{< callout "warning" >}}
One condition per combinator. Want AND logic? Chain two deciders in series. The first checks condition A, the second checks condition B. The final output is true only when both conditions pass.
{{< /callout >}}

{{< section "Arithmetic Combinator — The Calculator" >}}

The arithmetic combinator takes signals and performs math on them. Add, subtract, multiply, divide, modulo, exponent — it does all of them.

**Typical uses:**
- Count items on a belt segment
- Divide a signal to create thresholds (e.g., divide belt count by 60 for per-second rate)
- Convert signal types using "each to each" transformations
- Calculate ratios dynamically (e.g., multiply circuit count by 0.5 to estimate copper demand)

{{< recipe name1="decider" qty1="1x" name2="arithmetic" qty2="1x" name3="red_wire" qty3="10x" name4="green_wire" qty4="10x" result="circuit_network" rqty="1x" >}}

The arithmetic combinator shines when you need to convert signal types. Set it to "each + 0 output each" and suddenly everything connected converts to whatever channel you want. This is useful when you need to read belt contents across multiple segments — sum them all with one arithmetic combinator.

{{< section "Constant Combinator — Configuration Panel" >}}

The constant combinator outputs a fixed set of signals forever. No conditions, no math. Just constant values.

I use constant combinators for three things:
- Reference values in decider comparisons (e.g., set this to 100 and compare with actual production)
- Configuration flags (signal-green = 1 to enable night mode, red = 0 to disable)
- Test signals during debugging

A constant combinator paired with a decider is a one-way switch. The decider reads the constant value and compares it against a live signal. Change the constant value to change the behavior without rewiring anything.

{{< section "Persistence — Tick-Based Updates" >}}

Combinators update every game tick (60 times per second). A signal that changes on tick 1 propagates through a decider on tick 2, an arithmetic on tick 3, and reaches the final output on tick 4. For most applications this is instant. For high-speed belt counting it matters.

A feedback loop (wiring a combinator output back to its own input) creates memory. The combinator remembers its state from one tick to the next. This is the basis for SR latches, counters, and clocks.

{{< section "Build 1: Fluid Cracking Automation" >}}

The simplest practical circuit, and the one I use in every playthrough without exception.

1. Place a storage tank for heavy oil
2. Connect a red wire from the tank to a decider combinator
3. Set decider input: heavy_oil > 20000, output: heavy_oil = 1
4. Connect red wire from decider output to a pump on the heavy-to-light cracking line
5. Repeat for light oil to petroleum

When heavy oil exceeds 20000, the cracking pump activates. When it drops below, it stops. No wasted petroleum gas from over-cracking heavy oil when petroleum is not needed yet.

{{< diagram "diagrams/oil-cracking-circuit.svg" "Decider combinator controlling oil cracking based on storage tank level" "600" >}}

{{< callout "tip" >}}
Do the same for light oil to petroleum cracking: light_oil > 20000. Set petroleum cracking to run first, then light oil cracking kicks in automatically once petroleum demand is met. This priority system prevents lubricant starvation.
{{< /callout >}}

{{< section "Build 2: SR Latch for Nuclear Power" >}}

Nuclear reactors do not throttle. They burn 100% fuel cell or nothing. A simple SR Latch solves this by activating fuel insertion when steam drops below a threshold and deactivating when steam recovers.

This needs two decider combinators and a feedback loop:

1. Set decider: steam < 10000, output S = 1
2. Reset decider: steam > 24000, output R = 1
3. Wire both outputs to a third decider that acts as memory latch

The memory latch configuration:
- Input: S (from set), R (from reset)
- Condition: S > R, output S = 1
- Wire its output back to its own input (feedback loop)

When steam drops to 10000, the latch activates. Inserters feed one fuel cell. The latch stays on until steam reaches 24000, then resets. This saves enormous fuel over a simple timer-based approach.

{{< diagram "diagrams/sr-latch-nuclear.svg" "SR Latch circuit for nuclear reactor fuel control" "600" >}}

{{< section "Build 3: Belt Item Counting" >}}

Need to count items passing a point on a belt? Wire a belt segment to an arithmetic combinator set to "each + 0 output each". Wire the output back to the belt input (feedback loop). Every item that passes increments the counter.

To reset: connect a decider with condition "signal > target" that outputs a reset signal (red = 1). The counter clears to zero and starts fresh. This is useful for production statistics and train loading.

{{< section "Advanced: Clock and Timer Circuits" >}}

Need something to happen every 30 seconds? Build a clock circuit. A decider with its output wired back to its input increments a counter every tick.

Configuration:
- Input: signal-T connected from a constant combinator set to a negative reference
- Condition: signal-T < 1800 (30 seconds at 60 ticks per second)
- Output: signal-T = signal-T + 1

Feed the output to a second decider. When signal-T exceeds 1800, fire the conditioned event. Reset the clock by feeding a third decider that outputs a clear signal.

I use this to automate periodic rocket launches on Gleba. The clock triggers a launch every 3 minutes regardless of manual input.

{{< section "Common Mistakes" >}}

**Mixing red and green wires.** If both wires carry the same signal, combinators see both signals added together. Use one color per logical network.

**Feedback loop without a reset.** A feedback loop that never resets counts forever until it overflows. Signals max at 2^31 minus 1.

**Missing output wire.** You configured the combinator correctly but nothing happens. Check that the combinator output is wired to the target entity, not just a power pole.

**Forgetting entity settings.** The wire does not enable reading by itself. Go into the chest or inserter UI and enable "read contents" or "read hand contents".

**Over-engineering.** A single decider handles what most players try with three combinators. Start simple. Add complexity only when the simple solution does not work.

**Using both colors on the same network.** Red and green are two separate channels. Using both on the same group of entities means signals are duplicated. Stick to one color per network unless you have a specific reason.

{{< section "FAQ" >}}

**Q: Do red and green wires carry different signals?**
A: No. They carry the same signal types but in separate channels. Connect both to a combinator to read both channels simultaneously.

**Q: Can combinators output to a power pole?**
A: Yes. A combinator connected to a power pole sends its output to everything on that pole network.

**Q: How fast do combinators update?**
A: Every game tick (1/60 second). Each combinator in a chain adds one tick of delay.

**Q: Can I read a train cargo?**
A: Yes. Wire a train stop. In the train stop UI panel, enable "Read train contents." The stop outputs the cargo inventory as circuit signals.

**Q: What happens when the circuit network is overloaded?**
A: Factorio caps signals at 2^31 minus 1. If your counter exceeds this, it wraps around. Reset your counters before they hit this limit.

{{< section "Related Guides" >}}

- [Build a main bus with circuit-controlled logistics]({{< ref "base-design/main-bus-guide" >}})
- [Set up automated oil processing]({{< ref "production-ratios/oil-processing-guide" >}})
- [Use circuit conditions at train intersections]({{< ref "trains-logistics/basic-rail-network" >}})
- [Control nuclear fuel with SR latch]({{< ref "base-design/nuclear-power-guide" >}})
- [Automate platform logistics with circuits]({{< ref "space-age/space-platform-guide" >}})
