import xml.etree.ElementTree as ET

def find_one(xml):
    ent = xml.find('./crumbIssuer/excludeClientIPFromCrumb')

    if ent is not None:
        print(ent)
        print(ent.text)
        print(ent.attrib)


def traverse_doc(xml):
    print(f"Estamos em {xml.tag}")

    if xml.attrib:
        print(f"Os atributos são {xml.attrib}")

    if xml.text is not None and xml.text.strip() != '':
        print(f"Conteúdo: {xml.text}")

    print('-' * 50)

    for child in xml:
        traverse_doc(child)


def add_entity_and_save(doc, nome_arq):
    xml = doc.getroot()
    ent = xml.makeelement('MinhaTagAqui', {'xml': 'é um saco'})
    ent.text = 'Corram de Java'
    xml.append(ent)
    print(ent)
    ET.indent(doc, '    ')
    doc.write(nome_arq)

def main():
    nome_arq = 'jenkins.xml'

    with open(nome_arq) as arq_xml:
        doc_xml = ET.parse(arq_xml)

    root = doc_xml.getroot()
    # find_one(root)
    # traverse_doc(root)
    add_entity_and_save(doc_xml, nome_arq)


if __name__ == '__main__':
    main()
