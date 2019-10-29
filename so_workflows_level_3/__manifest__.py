{

    'name':'Sale Order WorkFlows (Level 3)',
    'description' : 'SO WorkFlows',
    'author' : 'Hafeez Brothers',
    'version': '1.0',
    'depends' : [
                   'base', 'product','sale',
                ],
    'data' :[   
                
                'views/sale_cust.xml',
                'security/hr_user_rights.xml'
            ],
    'installable' : True,
    'price':50.00,
    'currency':'EUR', 
    

}
