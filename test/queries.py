GET_ALL_COMPOUNDS = """
    query getAllCompounds {
        compounds {
            edges {
                node {
                    gskCompoundNum
                }
            }
        }
    }
""".strip()


GET_FIRST_COMPOUND = """
    query GetFirstCompound {
        compound {
            gskCompoundNum
        }
    }
""".strip()


GET_COMPOUND_BY_ID_USING_NODE = """
    query GetCompoundByNodeID($id: ID!) {
        node(id: $id) {
            ... on Compound {
                id
                gskCompoundNum
            }
        }
    }
""".strip()
