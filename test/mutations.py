CREATE_COMPOUND = """
    mutation CreateCompound {
        createCompound (input: {
            gskCompoundNum: "123456"
        }) {
            compound {
                gskCompoundNum
            }
        }
    }
""".strip()


UPDATE_COMPOUND = """
    mutation UpdateCompound ($id: String!, $input: UpdateCompoundInput!) {
        updateCompound (id: $id, input: $input) {
            compound {
                id
                gskCompoundNum
            }
        }
    }
""".strip()
