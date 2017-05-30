class AdressesController < ApplicationController

    def index
        @adresses = Adresse.all
    end

    def show
        @adresse = Adresse.find( params[:id] )
    end

    def new
        @adresse = adresse.new
    end

    def edit
        @adresse = adresse.find( params[:id] )
    end
end
