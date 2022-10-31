def house_type(df):
    
    single_house = df[(df.dependents == 'No') & (df.partner == 'No')]
    
    dual_house = df[(df.dependents == 'No') & (df.partner == 'Yes')]
    
    family_house = df[(df.dependents == 'Yes') & (df.partner == 'Yes')]
    
    single_head_house = df[(df.dependents == 'Yes') & (df.partner == 'No')]
    
    return df 
    
    
    
    
    
    
def single_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'No')]
    return df

def dual_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'Yes')]
    return df

def family_house(df):
    df = df[(df.dependents == 'Yes') & (df.partner == 'Yes')]
    return df

def single_head_house(df):
    df = df[(df.dependents == 'Yes') & (df.partner == 'No')]
    return df


    