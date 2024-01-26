from classes.classes import Page, Domaine

def get_pages_for_domain(session, domaine_id):
    """retourne une liste des pages d'un Domaine

    Args:
        session (Session): session en cours
        domaine_id (int): l'identifiant du domaine

    Returns:
        list: liste des Pages du Domaine
    """
    pages = session.query(Page).filter_by(domaine_id=domaine_id).all()
    return pages


if __name__=='__main__':
    from create_session import create_session
    session = create_session()
    pages =get_pages_for_domain(session, 1)
    print(pages[0].url)