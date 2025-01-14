# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    # informações em Amb. de desenvolvedor
    maestro.login(
        server="...", 
        login="...", 
        key="..."
    )
    # ID de uma tarefa em aguardo
    execution = maestro.get_execution("...")
    execution.task_id = "..."

    print(f"Tarefa: {execution.task_id}")

    enviar_item_unico(maestro)
    enviar_itens(maestro)
    puxa_um_item(maestro, execution)
    puxa_todos_itens(maestro, execution)


def enviar_item_unico(maestro):
    datapool = maestro.get_datapool(label="...")  # datapool label

    novo_item = DataPoolEntry(
        values={
            "nome": "item unico",
            "status": "status unico"
        }
    )
    datapool.create_entry(novo_item)


def enviar_itens(maestro):
    datapool = maestro.get_datapool(label="...")  # datapool label

    for item in range(5):
        novo_item = DataPoolEntry(
            values={
                "nome": f"item {item}",
                "status": f"status {item}"
            }
        )
        datapool.create_entry(novo_item)


def puxa_um_item(maestro, execution):
    datapool = maestro.get_datapool(label="...")  # datapool label

    item = datapool.next(task_id=execution.task_id)
    if item is None:
        print("não há itens")
        return

    # Processando item...
    print(f"""Item resgatado:
        {item['nome']}
        {item['status']}
          """)

    item.report_done()


def puxa_todos_itens(maestro, execution):
    datapool = maestro.get_datapool(label="...")  # datapool label

    while datapool.has_next():
        item = datapool.next(task_id=execution.task_id)
        if item is None:
            print("não há itens")
            break

        # Processando item...
        print(f"""Item resgatado:
            {item['nome']}
            {item['status']}
            """)

        item.report_done()


if __name__ == '__main__':
    main()
