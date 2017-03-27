# AlCaReco for track based alignment using J/Psi->MuMu events
import FWCore.ParameterSet.Config as cms

import HLTrigger.HLTfilters.hltHighLevel_cfi
ALCARECOTkAlJpsiMuMuHLT = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
    andOr = True, ## choose logical OR between Triggerbits
    eventSetupPathsKey = 'TkAlJpsiMuMu',
    throw = False # tolerate triggers stated above, but not available
    )

# DCS partitions
# "EBp","EBm","EEp","EEm","HBHEa","HBHEb","HBHEc","HF","HO","RPC"
# "DT0","DTp","DTm","CSCp","CSCm","CASTOR","TIBTID","TOB","TECp","TECm"
# "BPIX","FPIX","ESp","ESm"
import DPGAnalysis.Skims.skim_detstatus_cfi
ALCARECOTkAlJpsiMuMuDCSFilter = DPGAnalysis.Skims.skim_detstatus_cfi.dcsstatus.clone(
    DetectorType = cms.vstring('TIBTID','TOB','TECp','TECm','BPIX','FPIX',
                               'DT0','DTp','DTm','CSCp','CSCm'),
    ApplyFilter  = cms.bool(True),
    AndOr        = cms.bool(True),
    DebugOn      = cms.untracked.bool(False)
)

import Alignment.CommonAlignmentProducer.TkAlMuonSelectors_cfi
ALCARECOTkAlJpsiMuMuGoodMuons = Alignment.CommonAlignmentProducer.TkAlMuonSelectors_cfi.TkAlGoodIdMuonSelector.clone()

import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
ALCARECOTkAlJpsiMuMu = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone()
ALCARECOTkAlJpsiMuMu.filter = True ##do not store empty events

ALCARECOTkAlJpsiMuMu.ptMin = 0.8 ##GeV
ALCARECOTkAlJpsiMuMu.etaMin = -3.5
ALCARECOTkAlJpsiMuMu.etaMax = 3.5

ALCARECOTkAlJpsiMuMu.GlobalSelector.muonSource = 'ALCARECOTkAlJpsiMuMuGoodMuons'
# To not loose non-prompt J/Psi, do not apply any isolation
ALCARECOTkAlJpsiMuMu.GlobalSelector.applyGlobalMuonFilter = True

ALCARECOTkAlJpsiMuMu.TwoBodyDecaySelector.applyMassrangeFilter = True
ALCARECOTkAlJpsiMuMu.TwoBodyDecaySelector.minXMass = 2.7 ##GeV
ALCARECOTkAlJpsiMuMu.TwoBodyDecaySelector.maxXMass = 3.4 ##GeV

seqALCARECOTkAlJpsiMuMu = cms.Sequence(ALCARECOTkAlJpsiMuMuHLT+ALCARECOTkAlJpsiMuMuDCSFilter+ALCARECOTkAlJpsiMuMuGoodMuons+ALCARECOTkAlJpsiMuMu)
