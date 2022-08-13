ActiveAdmin.register Client do
  permit_params :pj_name, :client_name, :status, :order_date, :price, :memo
  # See permitted parameters documentation:
  # https://github.com/activeadmin/activeadmin/blob/master/docs/2-resource-customization.md#setting-up-strong-parameters
  #
  # Uncomment all parameters which should be permitted for assignment
  #
  # permit_params :pj_name, :client_name, :status, :order_date, :price, :memo
  #
  # or
  #
  # permit_params do
  #   permitted = [:pj_name, :client_name, :status, :order_date, :price, :memo]
  #   permitted << :other if params[:action] == 'create' && current_user.admin?
  #   permitted
  # end

  
end
