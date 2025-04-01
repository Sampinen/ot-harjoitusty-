sequenceDiagram

    participant Main as Main
    
    participant Kioski as Kioski
    
    participant hallinto as HKLLaitehallinto
    
    participant Lataaja as Lataajalaite
    
    participant Lukija as Lukijalaite
    
    participant kortti as Matkakortti
    
    Main ->> hallinto: lisaa_lataaja(rautatietori)
    
    Main ->> hallinto: lisaa_lukija(ratikka6)
    
    Main ->> Kioski: osta_matkakortti("Kalle")
    
    Kioski ->> Main: Matkakortti("Kalle")
    
    Main ->> Lataaja: lataa_arvoa(Matkakortti("Kalle"), 3)
    
    Lataaja ->> kortti: kasvata_arvoa(3)
    
    Main ->> Lukija: osta_lippu(Matkakortti("Kalle"), 0)
    
    Lukija ->> kortti: arvo()
    
    kortti ->> Lukija: 3
    
    Lukija ->> kortti: vahenna_arvoa(hinta)
    
    Lukija ->> Main: True
    
    Main ->> Lukija: osta_lippu(Matkakortti("Kalle"), 2)
    
    Lukija ->> kortti: arvo()
    
    kortti ->> Lukija: 1.5
    
    Lukija ->> Main: False
    
