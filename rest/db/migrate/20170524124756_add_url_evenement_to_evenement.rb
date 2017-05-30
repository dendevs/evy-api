class AddUrlEvenementToEvenement < ActiveRecord::Migration[5.0]
  def change
    add_column :evenements, :url_evenement, :string
  end
end
