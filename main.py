from rasa.shared.core.domain import Domain
import click


@click.command()
@click.option("--domain_folder")
def main(domain_folder):
    d = Domain.load(domain_folder)

    intents = sorted([i for i in d.intents if i in ['goodbye', 'greet', 'inform', 'affirm']])

    for i in intents:
        used_entities = sorted(d.intent_config(i)["used_entities"])

        print(f'intent: {i}')
        print(f'entities used:')
        for e in used_entities:
            print(f'  {e}')
        print('\n')
    
if __name__ == "__main__":
    main()