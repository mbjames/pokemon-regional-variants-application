import alolan_variant
import galarian_variant
import directory
import banner


def go_back():
    print("\n Would you like to go back? (y or n)")

    answer = input("\n > ").lower()

    if answer == 'y':
        start()

    elif answer == "n":
        exit()

    else:
        go_back()


def start():
    banner.print_banner()

    print("\n Welcome to the POKEMON REGIONAL VARIANT application.")
    print(" To view a pokemon directory select (v).")
    print(" To view a pokemon select (1 - 43).")
    print(" To exit select (q).")

    answer = input('\n > ').lower()

    if answer == 'v':
        directory.pokemon_directory()

        start()

    elif answer == 'q':
        exit()

    elif answer == "1":
        alolan_variant.alolan_rattata.print_alolan()

        go_back()

    elif answer == "2":
        alolan_variant.alolan_raticate.print_alolan()

        go_back()

    elif answer == "3":
        alolan_variant.alolan_raichu.print_alolan()

        go_back()

    elif answer == "4":
        alolan_variant.alolan_sandshrew.print_alolan()

        go_back()

    elif answer == "5":
        alolan_variant.alolan_sandslash.print_alolan()

        go_back()

    elif answer == "6":
        alolan_variant.alolan_vulpix.print_alolan()

        go_back()

    elif answer == "7":
        alolan_variant.alolan_ninetales.print_alolan()

        go_back()

    elif answer == '8':
        alolan_variant.alolan_diglett.print_alolan()

        go_back()

    elif answer == '9':
        alolan_variant.alolan_dugtrio.print_alolan()

        go_back()

    elif answer == '10':
        alolan_variant.alolan_meowth.print_alolan()

        go_back()

    elif answer == '11':
        alolan_variant.alolan_persian.print_alolan()

        go_back()

    elif answer == '12':
        alolan_variant.alolan_geodude.print_alolan()

        go_back()

    elif answer == '13':
        alolan_variant.alolan_graveler.print_alolan()

        go_back()

    elif answer == '14':
        alolan_variant.alolan_golem.print_alolan()

        go_back()

    elif answer == '15':
        alolan_variant.alolan_grimer.print_alolan()

        go_back()

    elif answer == '16':
        alolan_variant.alolan_muk.print_alolan()

        go_back()

    elif answer == '17':
        alolan_variant.alolan_exeggutor.print_alolan()

        go_back()

    elif answer == '18':
        alolan_variant.alolan_marowak.print_alolan()

        go_back()

    elif answer == '19':
        galarian_variant.galarian_meowth.print_galarian()

        go_back()

    elif answer == '20':
        galarian_variant.galarian_perrserker.print_galarian()

        go_back()

    elif answer == '21':
        galarian_variant.galarian_ponyta.print_galarian()

        go_back()

    elif answer == '22':
        galarian_variant.galarian_rapidash.print_galarian()

        go_back()

    elif answer == '23':
        galarian_variant.galarian_slowpoke.print_galarian()

        go_back()

    elif answer == '24':
        galarian_variant.galarian_slowbro.print_galarian()

        go_back()

    elif answer == '25':
        galarian_variant.galarian_farfetched.print_galarian()

        go_back()

    elif answer == '26':
        galarian_variant.galarian_sirfetchd.print_galarian()

        go_back()

    elif answer == '27':
        galarian_variant.galarian_weezing.print_galarian()

        go_back()

    elif answer == '28':
        galarian_variant.galarian_mr_mime.print_galarian()

        go_back()

    elif answer == "29":
        galarian_variant.galarian_mr_rime.print_galarian()

        go_back()

    elif answer == '30':
        galarian_variant.galarian_articuno.print_galarian()

        go_back()

    elif answer == '31':
        galarian_variant.galarian_zapdos.print_galarian()

        go_back()

    elif answer == '32':
        galarian_variant.galarian_moltres.print_galarian()

        go_back()

    elif answer == '33':
        galarian_variant.galarian_slowking.print_galarian()

        go_back()

    elif answer == '34':
        galarian_variant.galarian_corsola.print_galarian()

        go_back()

    elif answer == '35':
        galarian_variant.galarian_Cursola.print_galarian()

        go_back()

    elif answer == '36':
        galarian_variant.galarian_zigzagoon.print_galarian()

        go_back()

    elif answer == '37':
        galarian_variant.galarian_linoone.print_galarian()

        go_back()

    elif answer == '38':
        galarian_variant.galarian_obstagoon.print_galarian()

        go_back()

    elif answer == '39':
        galarian_variant.galarian_darumaka.print_galarian()

        go_back()

    elif answer == '40':
        galarian_variant.galarian_darmanitan.print_galarian()

        go_back()

    elif answer == '41':
        galarian_variant.galarian_yamask.print_galarian()

        go_back()

    elif answer == '42':
        galarian_variant.galarian_runerigus.print_galarian()

        go_back()

    elif answer == '43':
        galarian_variant.galarian_stunfisk.print_galarian()

        go_back()

    else:
        print("\n INVALID SELECTION!")

        start()


start()
