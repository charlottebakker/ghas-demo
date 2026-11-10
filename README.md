# GHAS-demo (oefenomgeving)

Deze publieke repository is uitsluitend een **niet-uitgerolde oefenomgeving**. De
Python-code bevat bewust een SQL-injection-risico; `requirements.txt` bevat bewust
een kwetsbare dependency. Draai of deploy deze code niet en gebruik er geen echte
gegevens of credentials mee.

## Voorbereiding (eenmalig)

1. Open **Settings > Advanced Security** en zet **CodeQL analysis > Set up >
   Default** aan. Wacht tot de analyse is afgerond; controleer daarna **Security >
   Code scanning**. [CodeQL instellen](https://docs.github.com/en/enterprise-cloud@latest/code-security/getting-started/quickstart-for-securing-your-repository#configuring-code-security)
2. Controleer onder **Settings > Advanced Security** dat **Dependency graph** en
   **Dependabot alerts** aanstaan. Wacht tot de dependency graph is bijgewerkt en
   controleer **Security > Dependabot**. [Dependabot alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/getting-started/quickstart-for-securing-your-repository#managing-dependabot-alerts)
3. Controleer onder **Settings > Advanced Security** dat **Secret Protection** en
   **Push protection** aanstaan. [Push protection instellen](https://docs.github.com/en/enterprise-cloud@latest/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enable-push-protection)

## Demo in ongeveer 10 minuten

1. **Code (3 min):** open **Security > Code scanning** en een alert in
   `demo_app.py`. Laat zien hoe gebruikersinvoer in de SQL-query terechtkomt.
   Vertel dat je de invoer in de praktijk via queryparameters moet doorgeven.
   [Code-scanning-alerts beoordelen](https://docs.github.com/en/enterprise-cloud@latest/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/assess-alerts)
2. **Dependencies (2 min):** open **Security > Dependabot** en bekijk een alert
   voor de bewust vastgepinde versie van `urllib3`. Bespreek de voorgestelde
   oplossing; wijzig de dependency niet in deze oefenrepository zolang je deze
   demo wilt herhalen. [Dependabot-alerts](https://docs.github.com/en/enterprise-cloud@latest/code-security/concepts/supply-chain-security/dependabot-alerts)
3. **Secrets (3 min):** laat **Settings > Advanced Security > Push protection**
   zien. Gebruik, als je de blokkade live wilt tonen, uitsluitend het **inactieve
   voorbeeldtoken** uit de officiële
   [GitHub Skills-oefening](https://github.com/skills/introduction-to-secret-scanning/blob/main/.github/steps/3-enable-push-protection.md):
   probeer het via de GitHub-webeditor in een nieuw bestand te committen en
   **annuleer** zodra de blokkade verschijnt. Bypass de blokkade niet en sla het
   bestand niet op. Gebruik nooit een echte sleutel.
4. **Afronding (2 min):** stel de klant de vraag welke van deze drie risico's
   vandaag het meest tijd kost: kwetsbare code, kwetsbare dependencies of gelekte
   secrets. Daarmee bepaal je het nuttigste vervolg.

De productindeling is belangrijk: **GitHub Code Security** omvat onder meer code
scanning; **GitHub Secret Protection** omvat onder meer secret scanning en push
protection. Dependabot alerts zijn niet exclusief voor een betaalde GHAS-licentie.
Voor private repositories gelden andere beschikbaarheidsvoorwaarden dan voor
publieke repositories. [Productoverzicht en beschikbaarheid](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security)
