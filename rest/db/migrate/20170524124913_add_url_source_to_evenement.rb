class AddUrlSourceToEvenement < ActiveRecord::Migration[5.0]
  def change
    add_column :evenements, :url_source, :string
  end
end
