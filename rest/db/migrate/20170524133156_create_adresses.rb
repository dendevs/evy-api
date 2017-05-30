class CreateAdresses < ActiveRecord::Migration[5.0]
  def change
    create_table :adresses do |t|
      t.string :pays
      t.string :province
      t.string :code_postal
      t.string :ville
      t.string :rue
      t.string :numero
      t.string :boite
      t.string :complement
      t.decimal :latitude , precision: 5, scale: 2
      t.decimal :longitude, precision: 5, scale: 2
      t.references :evenement, foreign_key: true

      t.timestamps
    end
  end
end
