class CreateClients < ActiveRecord::Migration[6.1]
  def change
    create_table :clients do |t|
      t.string :pj_name, null: false, defualt: ""
      t.string :client_name, null:false, default: ""
      t.integer :status, null: false, default: 0
      t.date :order_date, null: false
      t.bigint :price, null:false, defualt:0
      t.text :memo, null: true

      t.timestamps
    end
  end
end
