# Player Query Classification: AI vs. Rule/Database Lookup

This document establishes the boundary between static rule/database retrieval and generative/reasoning AI capabilities for TFT assistant queries.

| No. | TFT Player Query | Needs AI? | One-line Reason |
| :--- | :--- | :---: | :--- |
| 1 | "What is the recipe for Bloodthirster?" |  No | Static item formula directly retrievable from the game database. |
| 2 | "What are Ahri's best-in-slot items this set?" |  No | Best-in-slot data can be fetched directly from aggregated meta statistics APIs without reasoning. |
| 3 | "What is the rolling probability for 4-cost champions at level 7?" |  No | Roll odds per shop level are static, predefined game parameters. |
| 4 | "What stats does Bastion 4 provide?" |  No | Trait descriptions and tiered stat bonuses are static strings in the database. |
| 5 | "What is the difference between True Damage and Magic Damage?" |  No | Core game rules and damage mechanisms are documented factual definitions. |
| 6 | "At which round does the first Carousel stage take place?" |  No | Round/stage structure follows a fixed and deterministic match schedule. |
| 7 | "What effect does the 'Ticket to the Moon' augment have?" |  No | Augment description is fixed textual data in the patch reference. |
| 8 | "What is the total champion pool size for 5-cost units?" |  No | Champion pool sizes per tier are fixed integer constants. |
| 9 | "How many units are required to reach the maximum Noxus trait tier?" |  No | Trait breakpoint thresholds are structured tabular metadata. |
| 10 | "How much gold do I get for selling a 2-star 1-cost champion?" |  No | Champion sellback refund rules follow a fixed mathematical formula. |
| 11 | "I have 30 HP at level 7 with Ahri and Yasuo, how should I transition my board?" |  Yes | Requires situational board state evaluation, resource balancing, and tactical pivot planning. |
| 12 | "The top player is running 6 Mages with optimal items, how should I reposition to counter?" |  Yes | Involves dynamic spatial layout reasoning and adversarial board positioning analysis. |
| 13 | "Should I take an economy augment or combat augment when the lobby tempo is very fast?" |  Yes | Demands contextual evaluation of lobby pressure, health preservation, and risk trade-offs. |
| 14 | "Why is my 6 Brawler board on a losing streak in Stage 4 despite having full items?" |  Yes | Requires diagnosing multi-factor root causes such as damage scaling, item efficiency, and counter-matchups. |
| 15 | "Should I roll down to zero gold at round 3-2 when on a heavy loss streak?" |  Yes | Requires contextual risk analysis weighing stabilization odds against long-term economy depletion. |
| 16 | "I hit an early Fated Emblem, what is the smoothest transition path throughout the game?" |  Yes | Requires long-term composition planning and adaptive transition logic across stages. |
| 17 | "I only dropped AP components, but the shop only gives AD units. How should I play this?" |  Yes | Requires improvisational troubleshooting under unfavorable RNG to identify flexible slam or pivot lines. |
| 18 | "Why are high-elo players placing their primary frontline tank in row 2 instead of row 1 in this meta?" |  Yes | Requires contextual explanation of advanced unit targeting, aggro pathing, and meta nuances. |
| 19 | "Should I push fast level 8 or slow-roll for 3-star 3-cost carries in this game?" |  Yes | Depends on multi-agent game state: contestation rate, remaining health pool, and current copy counts. |
| 20 | "How do I recognize whether I should commit to a win streak or play for a lose streak from Stage 2?" |  Yes | Demands high-level strategic synthesis evaluating starting board strength relative to lobby power. |