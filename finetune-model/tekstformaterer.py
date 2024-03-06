import json
def create_template():
    with open("raw-text2.json", "r") as file:
        data = json.load(file)
        with open("instructed-trainingdata-flex2.jsonl", "w", encoding='utf8') as outfile:
            for line in data:
                print(line)
                dline = data[str(line)]
                print(data[str(line)])
                #system = data["system"]
                instruct = dline["instruct"]
                output = dline["output"]
                input = dline["input"]
                template = f"<s>[INST] <<SYS>>\n{system}\n<</SYS>>\n{instruct}\n{input}[/INST] {output} </s><s>"
                outfile.write(json.dumps(template, ensure_ascii=False) + "\n")

#instructions =

system = """You are trained to identify personal information.
Your work is to detect if the text contains personal information about the user. The categories are:
Personlig Identifiserbar Informasjon (PII): Dette inkluderer data som kan brukes til å unikt identifisere, kontakte, eller lokalisere en person. Eksempler inkluderer:
Navn, Hjemmeadresser, E-postadresser, Nasjonale identifikasjonsnummer, Seksuell legging, personnummer, Passnummer, Førerkortnummer, Telefonnummer, Fødselsdatoer.
Finansiell Informasjon: All informasjon relatert til en persons finansielle status eller transaksjoner bør maskeres. Eksempler inkluderer: Kreditt-/debetkortnummer, Bankkontonummer, Finansielle uttalelser, Kredittscore, Investeringdetaljer.
Helseinformasjon: Spesielt sensitiv på grunn av personvernlover som HIPAA (i USA), helse-relatert informasjon krever ofte maskering. Eksempler inkluderer: Pasientjournaler, Medisinsk historie, Reseptinformasjon, Forsikringsinformasjon.
Ansettelsesinformasjon: Personlige detaljer om en persons ansettelsesstatus eller -historie. Eksempler inkluderer: Lønnsinformasjon, Ansettelsesrekord, Prestasjonsevalueringer.
Utdanningsopptegnelser: Informasjon relatert til en students akademiske rekord. Dette kan inkludere: Karakterer, Transkripsjoner, Disiplinærrekorder, Opptaksopptegnelser.
Innloggingsdetaljer: Av sikkerhetsmessige årsaker bør innloggingsinformasjon alltid maskeres. Dette inkluderer: Brukernavn, Passord.
Forretningssensitiv Informasjon: Enhver proprietær eller konfidensiell forretningsinformasjon bør også vurderes, slik som: Forretningshemmeligheter, Interne finansielle rapporter, Konfidensielle forretningsstrategier, Ansatte liste.
"""
system2 = """
OPPGAVE: Du skal klassifisere personopplysninger i kategoriene:
- opplysninger om personlig
- opplysninger om arbeidsgiver
- helseopplysninger
- opplysninger om etnisk opprinnelse
- opplysninger om politisk oppfatning
- opplysninger om religion
- genetiske opplysninger
- opplysninger om seksuell legning eller forhold
Dersom teksten ikke inneholder personsensitiv informasjon skal du svare "tibakemeldingen inneholder ikke personopplysninger"

KONTEKST:
- Du er gitt en tilbakemelding på en webside fra bruker
- Tilbakemedlingen kan potensielt inneholde personopplysninger informasjon
"""

create_template()
