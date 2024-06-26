from enum import Enum

class Collection(Enum):
    ANIMAL_BEHAVIOR_AND_COGNITION   = "animal-behavior-and-cognition"
    BIOCHEMISTRY                    = "biochemistry"
    BIOENGINEERING                  = "bioengineering"
    BIOINFORMATICS                  = "bioinformatics"
    BIOPHYSICS                      = "biophysics"
    CANCER_BIOLOGY                  = "cancer-biology"
    CELL_BIOLOGY                    = "cell-biology"
    CLINICAL_TRIALS                 = "clinical-trials"
    DEVELOPMENTAL_BIOLOGY           = "developmental-biology"
    ECOLOGY                         = "ecology"
    EPIDEMIOLOGY                    = "epidemiology"
    EVOLUTIONARY_BIOLOGY            = "evolutionary-biology"
    GENETICS                        = "genetics"
    GENOMICS                        = "genomics"
    IMMUNOLOGY                      = "immunology"
    MICROBIOLOGY                    = "microbiology"
    MOLECULAR_BIOLOGY               = "molecular-biology"
    NEUROSCIENCE                    = "neurosciece"
    PALEONTOLOGY                    = "paleontology"
    PATHOLOGY                       = "pathology"
    PHARMACOLOGY_AND_TOXICOLOGY     = "pharmacology-and-toxicology"
    PHYSIOLOGY                      = "physiology"
    PLANT_BIOLOGY                   = "plant-biology"
    SCIENTIFIC_COMMUNICATION        = "scientific-communication-and-education"
    SYNTHETIC_BIOLOGY               = "synthetic-biology"
    ZOOLOGY                         = "zoology"

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

