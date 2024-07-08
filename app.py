from objects.dto import IFC_DTO
from utils.collector_mod import Collector

if __name__ == '__main__':
    collector = Collector('https://ca.finance.yahoo.com/quote/IFC.TO')
    data = collector.get_summary()

    dto = IFC_DTO.map_to_dto(data)

    print(data)

