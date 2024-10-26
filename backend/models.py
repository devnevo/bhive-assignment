from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    password: str
    
class Scheme(BaseModel):
    scheme_code: int = Field(alias="Scheme_Code")
    isin_div_payout: str = Field(alias="ISIN_Div_Payout_ISIN_Growth")
    isin_div_reinvestment: str = Field(alias="ISIN_Div_Reinvestment") 
    scheme_name: str = Field(alias="Scheme_Name") 
    net_asset_value: float = Field(alias="Net_Asset_Value") 
    date: str = Field(alias="Date")
    scheme_type: str = Field(alias="Scheme_Type")
    scheme_category: str = Field(alias="Scheme_Category")
    mutual_fund_family: str = Field(alias="Mutual_Fund_Family")