### Test-Driven Development i Python

Test-Driven Development(TDD) är en del av the Agile manifesto(https://agilemanifesto.org/) som togs fram på tidigt 2000-tal.

```html
Manifesto for Agile Software Development

We are uncovering better ways of developing
software by doing it and helping others do it.
Through this work we have come to value:

Individuals and interactions over processes and tools
Working software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over following a plan

That is, while there is value in the items on
the right, we value the items on the left more.

Kent Beck
Mike Beedle
Arie van Bennekum
Alistair Cockburn
Ward Cunningham
Martin Fowler
James Grenning
Jim Highsmith
Andrew Hunt
Ron Jeffries
Jon Kern
Brian Marick
Robert C. Martin
Steve Mellor
Ken Schwaber
Jeff Sutherland
Dave Thomas
```

 Anledningen till manifestet var att man ansåg att något var tokigt med  software-utveckling och behövde förändring. Man ansåg att utveckling av software inte alls kunde jämföras med utveckling av andra produkter, och att det därför krävdes en annan model för detta annat än det traditionella systemet.

I det traditionella systemet ligger begreppet "Waterfall methodology"

```pseudocode
-> Krav
	-> Design
		-> Kod
			-> Test
				-> Maintenance
```

Vi delade upp projektet i olika faser. Nästa fas kunde inte startas innan tidigare fas var klar.

Agile methodology bygger på en approach som delar upp ett projekt i  små etapper och förstår att ett projekts krav kan förändras längsmed.

Ur detta föddes andra agila metodologier så som Scrum och Kanban. Kent Beck, en av, och kanske den mest framstående, grundarna till the agile manifesto skapade sin egen: **Extreme Programming(XP)**.

XP bygger på Core Values, Core Principles och Core Practises

**Core Values**

Communication

Simplicity

Feedback

Courage

Respect

**Core Principles**

Baby steps

Quality

Flow

Improvement

Economics

Mutual Benefit

Accepted responsibility

**Core Practises**

Whole team

Test-first programming -> TDD

Incremental Design

Pair Programming

User Stories

Weekly Cycle

Continous Integration



### Test-Driven Development (TDD)

Test-Driven Development(TDD) handlar om att driva fram koden genom att skriva test före det att man skriver kod.

I TDD skriver man tester innan man skriver kod. När man har skrivit ett test skriver man kod för att få testet att gå igenom. En viktig teknik i detta är  **red-green testing**.

Vi får testet att *fail* innan vi ens har skrivit en rad kod. Det är viktigt att tester fail av rätt orsaker. För att försäkra sig om detta så skriver man vad som kallas för en *shell function*. En shell function innehåller ingenting annat än sin funktion.

###### Red-Green Testing

**./greeting**

**greeting.py**

```python
def greeting(name):
  pass
```

Därefter skiver vi vårt test.

**test_greeting.py**

```python
from greeting import greeting
import unittest

class TestGreeting(unittest.TestCase):
  def test_greeting(self):
    msg = greeting("Alex")
    self.assertEqual(msg, "Greetings Alex")
```

**terminal**

```
python -m unittest test_greeting.py
```

```
alexs-MacBook-Pro% python -m unittest test_greeting.py
F
======================================================================
FAIL: test_greeting (test_greeting.TestGreeting)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/alex/Documents/projects/tdd-python/greeting/test_greeting.py", line 7, in test_greeting
    self.assertEqual(msg, "Greetings Alex")
AssertionError: None != 'Greetings Alex'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

**greeting.py**

```python
def greeting(name):
  return f"Greetings {name}"
```



```
alexs-MacBook-Pro% python -m unittest test_greeting.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

###### Varför TDD?

Rent arbetsmässigt så skapar det en goare arbetssprocess. Vi får en liten kick varje gång ett test pass. Att skriva test i slutet av ett projekt skulle garanterat kännas som en börda. Genom att baka in test i utvecklingsprocessen får vi ett mer effektivt och roligare arbetssätt.

När vi redan har satt upp test så har vi möjlighet att *refactor* och testa på nya funktionaliteter utan att behöva oroa oss för att något skulle förstöras vid implementering.

###### The Three Laws of TDD

http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd

```
1. You are not allowed to write any production code unless it is to make a failing unit test pass.

2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.

3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.
```

### CI

Continuos Integration är även det ett agile mindset och en del av XP. Det är bästa praxis för DevOps att i små etapper integrera kodförändringar till *main branch* och att testa ändringarna så tidigt och ofta som möjligt

**Continuous Integration**

- Frequent merges to main branch
- Automated unit testing

**Continuous Delivery**

- Short release shedules

###### Varför?

Innan vi funderar på hur bör vi fundera kring varför. Innan the agile manifesto går det att tänka sig att utvecklingen såg annorlunda ut; ett gäng utvecklare jobbade på samma kod, och när dem integrerade sin kod, så fallerade allting och det var svårt att felsöka på var felet låg.

Nu har man ett repository där koden lagras. Alla i teamet jobbar på sin version av koden; en feature, branch eller vad det än kan tänkas vara. Vad som händer är att dessa förändringar som utvecklarna arbetar med frekvent mergas ihop med Koden, så att man försäkrar sig om att alla åtminstone arbetar på hyfsat likadana versioner av applikationen.

En annan viktig byggsten i CI är **automated unit testing**. Unit testing handlar om att verifierara att varje liten del/komponent av ett program funkar som det ska.

###### Github Actions

Github Actions låter oss sätta upp ett workflow där till exempel varje gång någon pushar till ett github repo, så ska något automatiskt hända.

För att sätta upp ett sådant workflow använder vi oss av en yaml-fil. YAML används ofta för konfiguration

```yaml
key1: value1
key2: value2
key3:
		- item1
		- item2
		- item3
```

###### .github/workflows/ci.yml

```yaml
name: testing
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Python 3
        uses: actions/setup-python@v1
        with:
          python-version: 3.6
      - name: Run tests with pytest
        run: python discover -s ./Tests
```

###### Dockerize it































